from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = APIFlask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class UserIn(Schema):
    email = String(required=True, validate=Length(0, 80))
    password = String(required=True, validate=Length(0, 120))

class UserOut(Schema):
    id = Integer()
    email = String()

@app.post('/user')
@app.input(UserIn)
@app.output(UserOut)
def cadastrar(json_data):
    try:
        user = User(email=json_data['email'], password=json_data['password'])
        db.session.add(user)
        db.session.commit()
        return user, 201
    except:
        return abort(400, message="Email já cadastrado")

@app.get('/user/<email>')
@app.output(UserOut)
def get_user(email):
    user = User.query.filter_by(email=email).first()
    if user is None:
        return abort(404, message="Usuário não encontrado")
    return user



if __name__ == '__main__':
    app.run(debug=True, port=5001)