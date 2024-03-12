# 🚀 Configuração do Projeto

## 📚 Explicações
Este projeto foi criado com o objetivo de compartilhar conhecimentos sobre Flask. Ele inclui a criação de uma página de login e cadastro de usuários, uma API para manipulação de dados, e utiliza SQLite para armazenar os dados dos usuários. Para estilização, foi usado o framework TailwindCSS.

Além disso, o projeto explora conceitos de arquitetura de software, como MVC e Blueprints. Para demonstrar a diferença entre eles, foram criadas três branches paralelas:

- [Blueprint](https://github.com/GetulioLT/Sistema-Login/tree/blueprints)
- [MVC](https://github.com/GetulioLT/Sistema-Login/tree/mvc)
- [MVC-Blueprint](https://github.com/GetulioLT/Sistema-Login/tree/mvc-blueprint)

Cada branch tem o objetivo de mostrar uma abordagem diferente de arquitetura e organização de código.

O guia a seguir irá ajudá-lo a configurar e testar o projeto em sua máquina.

## 🛠️ Pré-requisitos
Certifique-se de ter o Python, pip e o git instalados em seu sistema.

## 📥 Download do Projeto
Primeiro, com o git instalado, você pode clonar o projeto com o seguinte comando:

```bash
git clone https://github.com/GetulioLT/Sistema-Login.git
```

## 🌐 Criação e Ativação do Ambiente Virtual
1. Com o projeto clonado, abra o terminal e navegue até a pasta do projeto. Em seguida, crie um ambiente virtual com o seguinte comando (substitua "version" pela versão do Python que você está utilizando):

```bash
python -version -m venv venv
```
2. Ative o ambiente virtual:

```bash
venv/bin/activate
```

## 📦 Instalação das Dependências
Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## 🗄️ Configuração do Banco de Dados
Navegue até a pasta api e execute os seguintes comandos:

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

## 🚀 Execução da API e do Frontend
1. Com o banco de dados configurado, execute a API:

```bash
cd api
python app.py
```

2. Com a API em execução, abra um novo terminal, navegue até a pasta raiz e execute o frontend:

```bash
python app.py
```

## 🌐 Acesso ao Sistema e à API

Com a API e o Frontend em execução, você pode acessar:

- O sistema de login e cadastro através do seguinte endereço:

```bash
http://localhost:5000
```

- A API através do seguinte endereço:

```bash
http://localhost:5001
```

## 📜 Licença
Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE.md) para obter detalhes.

## 👨‍💻 Autor
Feito por Getulio Vagner Miranda Santos. 
- GitHub: [GetulioLT](https://github.com/GetulioLT)
- LinkedIn: [Getulio Vagner](https://www.linkedin.com/in/getulio-vagner-117341186/)

