# Minha Matrícula
Buscador que auxilia estudantes da Universidade de Brasília a encontrarem disciplinas.

## Ambiente de desenvolvimento

Clone o repositório.

```
git clone https://github.com/mds-trindadev/minha-matricula.git
```

```
cd minha-matricula
```

### Backend

#### pip

Atualize a lista das versões dos pacotes disponíveis.

```
sudo apt update
```

Instale o pip.
```
sudo apt install python3-pip
```

Atualize o pip.
```
pip3 install --upgrade pip
```

#### Virtualenv

Atualize a lista das versões dos pacotes disponíveis.

```
sudo apt update
```

Instale o Virtualenv.

```
pip3 install virtualenv
```

Crie um ambiente virtual.

```
cd backend/
```
```
virtualenv env
```

Ative o ambiente.
```
source env/bin/activate
```

#### Requisitos

Instale os requisitos.
```
pip3 install -r requirements.txt
```

#### Execução

```
python3 run.py
```

### Frontend

Entre na pasta do frontend.

```
cd frontend/
```

#### Node.js e npm
Se não possuir o Node.js e o npm, instale utilizando o nvm.

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash
```
Feche e abra o terminal.

```
nvm install 'lts/*'
```
Verifique a instalação.

```
npm --version && node --version
```
 
#### Ambiente de desenvolvimento
 
Em `frontend/`

 ```
npm install
```

Para executar

```
npm run serve
```
