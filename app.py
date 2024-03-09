from flask import Flask, render_template, request, redirect, url_for

from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

import requests

app = Flask(__name__)
app.secret_key = "jason"

login_manager = LoginManager()
login_manager.init_app(app)

# Define uma classe de usuário que herda de UserMixin
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Função para carregar um usuário com base no ID
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def login():
    return render_template('login.html')

@app.route("/login-in", methods=["POST"])
def login_in():
    email = request.form["email"]

    try:
        # Faz uma requisição para verificar o usuário
        login_response = requests.get(f"http://localhost:5001/user/{email}")
    except Exception as e:
        return redirect(url_for('login'))

    try:
        email = login_response.json()["email"]

        user = User(email)
        login_user(user)

        return redirect(url_for('home'))
    except Exception as e:
        return redirect(url_for('login'))

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route("/cadastro-in", methods=["POST"])
def cadastro_in():
    email = request.form["email"]
    password = request.form["password"]

    data = {
        "email": email,
        "password": password
    }

    # Faz uma requisição para cadastrar o usuário
    cadastro_response = requests.post("http://localhost:5001/user", json=data)
    try:
        cadastro_response.json()["email"]
        return redirect(url_for('login'))
    except Exception as e:
        return redirect(url_for('cadastro'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)