from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = APIFlask(__name__)  # Cria uma instância da aplicação Flask usando APIFlask

# Configurações do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializações do SQLAlchemy e do Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Definição do modelo de usuário
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Esquema para entrada de dados do usuário
class UserIn(Schema):
    email = String(required=True, validate=Length(0, 80))
    password = String(required=True, validate=Length(0, 120))

# Esquema para saída de dados do usuário
class UserOut(Schema):
    id = Integer()
    email = String()

# Rota para cadastrar um usuário
@app.post('/user')
@app.input(UserIn)
@app.output(UserOut)
def cadastrar(json_data):
    try:
        user = User(email=json_data['email'], password=json_data['password'])
        db.session.add(user)
        db.session.commit()
        return user, 201  # Retorna o usuário cadastrado com o código de status HTTP 201 (Created)
    except:
        return abort(400, message="Email já cadastrado")  # Aborta a requisição com o código de status HTTP 400 (Bad Request)

# Rota para obter informações de um usuário pelo email
@app.get('/user/<email>')
@app.output(UserOut)
def get_user(email):
    user = User.query.filter_by(email=email).first()
    if user is None:
        return abort(404, message="Usuário não encontrado")  # Aborta a requisição com o código de status HTTP 404 (Not Found) se o usuário não for encontrado
    return user  # Retorna as informações do usuário

# Executa o aplicativo Flask em modo de depuração na porta 5001
if __name__ == '__main__':
    app.run(debug=True, port=5001)
