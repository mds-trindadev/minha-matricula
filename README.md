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

# frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
```