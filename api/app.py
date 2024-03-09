from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_httpauth import HTTPBasicAuth

app = APIFlask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username == 'admin' and password == 'admin':
        return True
    return False

# Esquema para validação de entrada de dados do usuário
class UserIn(Schema):
    email = String(required=True, validate=Length(10, 50))
    password = String(required=True, validate=Length(8, 24))

# Esquema para formatação de saída de dados do usuário
class UserOut(Schema):
    id = Integer()
    email = String()
    password = String()

# Modelo de usuário para o SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Rota para cadastrar um usuário
@app.post('/user')
@app.input(UserIn)
@app.output(UserOut)
def cadastrar(json_data):
    try:
        user = User(email=json_data['email'], password=json_data['password'])
        db.session.add(user)
        db.session.commit()
        return user, 201
    except Exception as e:
        return abort(400, message=f"Email já cadastrado,\n {e}")

# Rota para obter informações de um usuário pelo email
@app.get('/user/<email>')
@app.output(UserOut)
def get_user(email):
    user = User.query.filter_by(email=email).first()
    if user is None:
        return abort(404, message="Usuário não encontrado")
    return user, 200

# Rota para reiniciar o banco de dados
@app.get('/reset-db')
@auth.login_required
def reset_db():
    db.drop_all()
    db.create_all()
    return "Banco de dados reiniciado com sucesso", 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)