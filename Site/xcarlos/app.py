from flask import Flask, render_template, request, url_for, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'chave_supersecreta'
import database


@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        form = request.form

        if database.cadastro(form):
            return redirect(url_for('home'))
        else:
            return "erro1"

    return render_template('login.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = request.form

        if database.login(form) == True:
            session['email'] = form['email']
            return redirect(url_for('home'))
        else:
            return "erro2"

    if request.method == "GET":
        return render_template('login.html')

@app.route('/home')
def home():
    if 'email' not in session:
        return redirect(url_for('login'))
    
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)