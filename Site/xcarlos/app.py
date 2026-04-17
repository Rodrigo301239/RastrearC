from flask import Flask, render_template, request, url_for, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'chave_supersecreta'
import database


@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/cadastro',methods = ["GET","POST"])
def cadastrar():
    form = request.form
    if database.cadastro(form) == True:
        return render_template('home.html')
    
    else:
        return ("erro1")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = request.form

        if database.login(form) == True:
            session['email'] = form['email']
            return redirect(url_for('home'))
        else:
            return "erro2"

    # 👇 quando acessar pelo link (GET)
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)