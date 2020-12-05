from app.controllers.turma import Disciplina
from app.controllers.turma import Departamento

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import json
import re

class Graph:

    def __init__(self, v):
        self.V = v
        self.listaVertices = []
        self.numV = 0
        self.adj = []
        self.tc = []

        for i in range(self.V):
            self.adj.append([0] * self.V)
            self.tc.append([0] * self.V)

    def adicionaVertice(self, vertice):
        self.numV += 1
        self.listaVertices.append(vertice)

    def getindex(self, nome):
        i = 0
        for i in range(self.numV):
            if nome == self.listaVertices[i]['nome']:
                break
            else:
                i = -1

        return i

    def adicionaAresta(self, inicio, fim):
        self.adj[fim][inicio] = 1

    def Gerartc(self):
        for i in range(self.numV):
            for j in range(self.numV):
                self.tc[i][j] = self.adj[i][j]

        for i in range(self.numV):
            self.tc[i][i] = 1

        for i in range(self.numV):
            for s in range(self.numV):
                if self.tc[s][i] == 1:
                    for t in range(self.numV):
                        if self.tc[i][t] == 1:
                            self.tc[s][t] = 1

    def geradorGrauTrancamento(self):
        for i in range(self.numV):
            aux = 0
            for j in range(self.numV):
                if self.tc[j][i] == 1:
                    aux += 1

            self.listaVertices[i]['grauTrancamento'] = aux

    def buscarDisciplina(self, codigo):
        campus = codigo[:3]

        # Referencia a no do banco de dados
        ref = db.reference('/disciplina/' + campus + '/' + codigo)
        disciplinas = ref.get()

        if disciplinas:
            temp = ''     
            if 'preRequisitos' in disciplinas:
                temp = disciplinas['preRequisitos']
            else:
                temp = 'Indisponivel'

            return temp

    def buscarBancodeDados(self):
        ref = db.reference('/curso/')
        cursos = ref.get()

        vetorCursos = {}
        for fluxo in cursos:
            # Percorre cada curso
            vetorFluxo = []
            u = 1
            for i in cursos[fluxo]:
                # Percorre cada fluxo
                if i:
                    for j in i:
                        # Percorre cada semestre
                        if i[j] == 'OB':
                            x = u
                            temp = {'codigo': j, 'semestre': x}
                            vetorFluxo.append(temp)
                    u += 1
            vetorCursos[fluxo] = vetorFluxo

        dictCursos = {}

        n = 0
        for i in vetorCursos:
            # Percorre cada curso
            dictCodigos = {}
            for j in vetorCursos[i]:
                # Percorre cada disciplina
                k = {'nome': j['codigo'], 'grauTrancamento': 0, 'semestre': j['semestre']}
                self.adicionaVertice(k)
                preRequisitos = str(self.buscarDisciplina(j['codigo']))
                temp = re.findall(r'[A-Z]{3}[0-9]{4}', preRequisitos)
                dictCodigos[j['codigo']] = temp
                dictCursos[i] = dictCodigos


            for g in dictCodigos:
                for j in dictCodigos[g]:
                    x = self.getindex(j)
                    z = self.getindex(g)
                    self.adicionaAresta(x, z)

            self.Gerartc()
            self.geradorGrauTrancamento()
            tempGT = self.listaVertices

            for e in tempGT:
                ref = db.reference('/trancamento/'+i+'/'+str(e['semestre'])+'/'+e['nome'])
                ref.update({'grauTrancamento': e['grauTrancamento'], 'cursada': 0})

            #zerar grafo
            self.__init__(100)
        return