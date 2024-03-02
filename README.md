# Passo a Passo

## 1. Criação da Venv
```bash
py -versao -m venv venv
```

## 2. Ativação da Venv
```bash
venv\Scripts\activate
```

## 3. Instalação das Dependências
```bash
pip install -r requirements.txt
```

## 4. Criação do Banco de Dados
```bash
cd api
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

## 5. Execução da Aplicação
Para a execução da aplicação, é necessário executar o arquivo app.py, que se encontra na pasta api, em um terminal diferente do app.py que se encontra na pasta raiz do projeto.:
```bash
cd api
python app.py
```

## 6. Execução do Frontend
Para a execução do frontend, é necessário executar o arquivo app.py, que se encontra na pasta raiz do projeto, em um terminal diferente do app.py que se encontra na pasta api.:
```bash
python app.py
```