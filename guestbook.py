from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']
    return render_template ( 'index.html', name=name, comment=comment)

@app.route('/home', methods=['GET'])
def home():
    return render_template('example.html',links=["https://www.google.com/","https://www.youtube.com/watch?v=HILynX3Dsoc"])


if __name__ =='__main__':
    app.run(debug=True)