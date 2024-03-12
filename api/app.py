# Importando as bibliotecas necessárias
from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from flask_httpauth import HTTPBasicAuth

# Criando uma instância da classe APIFlask
app = APIFlask(__name__)

# Configurando a URI do banco de dados e desativando o rastreamento de modificações do SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o SQLAlchemy e o Migrate com a aplicação
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Criando uma instância da classe HTTPBasicAuth
auth = HTTPBasicAuth()

# Definindo a função de verificação de senha para a autenticação básica HTTP
@auth.verify_password
def verify_password(username, password):
    if username == 'admin' and password == 'admin':
        return True
    return False

# Definindo o esquema de entrada de dados do usuário
class UserIn(Schema):
    email = String(required=True, validate=Length(10, 50))
    password = String(required=True, validate=Length(8, 24))

# Definindo o esquema de saída de dados do usuário
class UserOut(Schema):
    id = Integer()
    email = String()
    password = String()

# Definindo o modelo de usuário para o SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Definindo a rota para cadastrar um usuário
@app.post('/user')
@app.input(UserIn)
@app.output(UserOut)
def cadastrar(json_data):
    try:
        user = User(email=json_data['email'], password=json_data['password'])
        db.session.add(user)
        db.session.commit()
        return user, 201
    except IntegrityError:
        return abort(400, message="Email já cadastrado")

# Definindo a rota para obter informações de um usuário pelo email
@app.get('/user/<email>')
@app.output(UserOut)
def get_user(email):
    user = User.query.filter_by(email=email).first()
    if user is None:
        return abort(404, message="Usuário não encontrado")
    return user, 200

# Definindo a rota para reiniciar o banco de dados
@app.get('/reset-db')
@auth.login_required
def reset_db():
    db.drop_all()
    db.create_all()
    return "Banco de dados reiniciado com sucesso", 200

# Iniciando a aplicação
if __name__ == '__main__':
    app.run(debug=True, port=5001)