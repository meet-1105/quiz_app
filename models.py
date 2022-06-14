from routes import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    contact_no = db.Column(db.Integer, nullable=False)
    user_result = db.Column(db.String(200))
    score = db.Column(db.Integer)


class Subject(db.Model):
    id = db.Column(db.Integer, unique=True, autoincrement=True)
    sub_name = db.Column(db.String(20), primary_key=True)


class QA(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sub_name = db.Column(db.String(20), db.ForeignKey(Subject.sub_name), nullable=False)
    question = db.Column(db.String(100), nullable=False)
    options = db.Column(db.String(200), nullable=False)
    correct_opt = db.Column(db.String(70), nullable=False)
