from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

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
    response = requests.post("http://localhost:5001/user", json=data)
    try:
        email_ca = response.json()["email"]
        print(f"Email {email_ca} cadastrado com sucesso!")
        return redirect(url_for('login'))
    except:
        print("Email já cadastrado")
        return redirect(url_for('cadastro'))
    
@app.route("/login-in", methods=["POST"])
def login_in():
    email = request.form["email"]
    response = requests.get(f"http://localhost:5001/user/{email}")
    try:
        email = response.json()["email"]
        print(f"Usuário {email} encontrado!")
        return redirect(url_for('login'))
    except:
        print("Usuário não encontrado")
        return redirect(url_for('cadastro'))

if __name__ == '__main__':
    app.run(debug=True)