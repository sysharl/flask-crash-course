from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env

app = Flask(__name__)

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))

@app.route('/')
def index():
    results = Comments.query.all()
    return render_template('index.html',result= results)

@app.route('/sign')
def sign():
    return render_template('sign.html')


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']
    signature = Comments(name=name, comment=comment)
    db.session.add(signature)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/home', methods=['GET'])
def home():
    return render_template('example.html',links=["https://www.google.com/","https://www.youtube.com/watch?v=HILynX3Dsoc"])

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)