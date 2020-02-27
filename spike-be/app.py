
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy, inspect

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'false'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@localhost/spike'
db = SQLAlchemy(app)
CORS(app, supports_credentials=True)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    about = db.Column(db.String, nullable=False)
    funfact = db.Column(db.String, nullable=False)
    other = db.Column(db.String, nullable=False)
    instagram = db.Column(db.String, nullable=True)
    twitter = db.Column(db.String, nullable=True)
    github = db.Column(db.String, nullable=True)
    linkedin = db.Column(db.String, nullable=True)

    def __init__(self, email, name, password, about, funfact, other, instagram, twitter, github, linkedin):
      self.email = email
      self.name = name
      self.password = password
      self.about = about
      self.funfact = funfact
      self.other = other
      self.instagram = instagram
      self.twitter = twitter
      self.github = github
      self.linkedin = linkedin
      pass

    @property
    def serialize(self):
       return {
        'id' : self.id,
        'email' : self.email,
        'name' : self.name,
        'password' : self.password,
        'about': self.about,
        'funfact' : self.funfact,
        'other' : self.other,
        'instagram':self.instagram,
        'twitter':self.twitter,
        'github':self.github,
        'linkedin':self.linkedin
       }

@app.route("/logIn", methods=['GET'])
def login():
  email = request.args.get('email')
  password = request.args.get('password')
  q = Users.query.filter(Users.email == email, Users.password == password).first()
  return jsonify(json_list=[q.serialize])

@app.route('/updatePW', methods=['PUT'])
def updatePW():
  if request.method == "PUT":
    body = request.get_json(force=True)
    q = Users.query.get(body['id'])
    setColumns(Users, q, body)
    db.session.commit()
    q = Users.query.get(body['id'])
    return jsonify(json_list=[q.serialize])

@app.route('/updateUser', methods=['PUT'])
def update():
  if request.method == "PUT":
    body = request.get_json(force=True)
    q = Users.query.get(body['id'])
    setColumns(Users, q, body)
    db.session.commit()
    q = Users.query.get(body['id'])
    return jsonify(json_list=[q.serialize])

@app.route('/signup', methods=["POST"])
def signup():
  if request.method == "POST":
    body = request.get_json(force=True)
    user = Users(
      email=body['email'], 
      name=body['name'],
      password=body['password'],  
      about=body['about'],  
      funfact=body['funfact'],  
      other=body['other'],
      instagram=body['instagram'],
      twitter=body['twitter'],
      github=body['github'],
      linkedin=body['linkedin']
    )
    name=body['name']
    password=body['password']
    try:
      db.session.add(user)
      db.session.commit()
    except:
      return {
        "error": f"A user with {body['email']} already exists"
      }
    db.session.refresh(user)
    q = Users.query.filter(Users.name == name, Users.password == password).first()
    return jsonify(json_list=[q.serialize])

def setColumns(table, model, body):
  myMap = inspect(table)
  for col in myMap.attrs:
    try:
      setattr(model, col.key, body[col.key])
    except:
      continue
