from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')  # Rota para a página de login

@app.route("/login-in", methods=["POST"])
def login_in():
    email = request.form["email"]
    response = requests.get(f"http://localhost:5001/user/{email}")  # Envia uma requisição GET para o servidor de login
    try:
        email = response.json()["email"]
        print(f"Usuário {email} encontrado!")  # Imprime mensagem se o usuário for encontrado
        return redirect(url_for('login'))  # Redireciona para a página de login após o login bem-sucedido
    except:
        print("Usuário não encontrado")  # Imprime mensagem se o usuário não for encontrado
        return redirect(url_for('cadastro'))  # Redireciona para a página de cadastro se o usuário não for encontrado


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')  # Rota para a página de cadastro

@app.route("/cadastro-in", methods=["POST"])
def cadastro_in():
    email = request.form["email"]
    password = request.form["password"]
    data = {
        "email": email,
        "password": password
    }
    response = requests.post("http://localhost:5001/user", json=data)  # Envia uma requisição POST para o servidor de cadastro
    try:
        email_ca = response.json()["email"]
        print(f"Email {email_ca} cadastrado com sucesso!")  # Imprime mensagem se o cadastro for bem-sucedido
        return redirect(url_for('login'))  # Redireciona para a página de login após o cadastro bem-sucedido
    except:
        print("Email já cadastrado")  # Imprime mensagem se o email já estiver cadastrado
        return redirect(url_for('cadastro'))  # Redireciona de volta para a página de cadastro em caso de falha no cadastro


if __name__ == '__main__':
    app.run(debug=True)  # Executa o aplicativo Flask em modo de depuração
