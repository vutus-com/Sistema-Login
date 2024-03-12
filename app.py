# Importando as bibliotecas necessárias
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
import requests

# Criando uma instância da classe Flask
app = Flask(__name__)

# Definindo a chave secreta da aplicação
app.secret_key = "jason"

# Criando uma instância da classe LoginManager
login_manager = LoginManager()

# Inicializando o gerenciador de login com a aplicação
login_manager.init_app(app)

# Definindo uma classe de usuário que herda de UserMixin
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Definindo a função que carrega um usuário com base no ID
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Definindo a rota para a página de login
@app.route('/')
def login():
    return render_template('login.html')

# Definindo a rota para fazer login
@app.route("/login-in", methods=["POST"])
def login_in():
    email = request.form["email"]

    # Fazendo uma requisição GET para obter informações do usuário
    response = requests.get(f"http://localhost:5001/user/{email}")
    if response.status_code == 200:
        user = User(email)
        login_user(user)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

# Definindo a rota para a página de cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# Definindo a rota para fazer cadastro
@app.route("/cadastro-in", methods=["POST"])
def cadastro_in():
    email = request.form["email"]
    password = request.form["password"]

    data = {
        "email": email,
        "password": password
    }

    # Fazendo uma requisição POST para cadastrar o usuário
    response = requests.post("http://localhost:5001/user", json=data)
    if response.status_code == 200:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('cadastro'))

# Definindo a rota para a página inicial
@app.route('/home')
@login_required
def home():
    return render_template('home.html')

# Definindo a rota para fazer logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Iniciando a aplicação
if __name__ == '__main__':
    app.run(debug=True)