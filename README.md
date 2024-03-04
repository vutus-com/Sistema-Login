# Configuração do Projeto

Este guia passo a passo irá ajudá-lo a configurar e executar o projeto.

## Pré-requisitos

Certifique-se de ter o Python e o pip instalados em seu sistema.

## 1. Criação do Ambiente Virtual

Primeiro, vamos criar um ambiente virtual para isolar as dependências do nosso projeto. No terminal, execute o seguinte comando:

```bash
py -m venv venv
```

## 2. Ativação do Ambiente Virtual

Agora, vamos ativar o ambiente virtual com o seguinte comando:

```bash
venv\Scripts\activate
```

## 3. Instalação das Dependências

Com o ambiente virtual ativado, podemos instalar as dependências necessárias para o projeto. As dependências estão listadas no arquivo requirements.txt. Para instalá-las, execute o seguinte comando:

```bash
pip install -r requirements.txt
```

## 4. Configuração do Banco de Dados

Vamos configurar o banco de dados. Navegue até a pasta api e execute os seguintes comandos:

```bash
cd api
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

## 5. Execução da API

Para executar a API, você precisará executar o arquivo app.py na pasta api. Certifique-se de fazer isso em um terminal separado. Aqui está o comando:

```bash
cd api
python app.py
```

## 6. Execução do Frontend

Para executar o frontend, você precisará executar o arquivo app.py na pasta raiz do projeto. Faça isso em um terminal diferente do que você usou para a API. Aqui está o comando:

```bash
python app.py
```

## 7. Acessando a Aplicação

Agora que a API e o frontend estão em execução, você pode acessar a aplicação em seu navegador. Abra o seguinte link:

```bash
http://localhost:5000
```

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE.md](LICENSE.md) para obter detalhes.

## Autor

- **Getulio Vagner** - GetulioLT(github)

