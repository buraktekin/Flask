from flask import Flask, request, render_template, flash, session

app = Flask(__name__)
app.secret_key = 'secret'

users = {'burak': 'burak123', 'berk': 'berk123', 'cenk' : 'cenkalti', 'ferit' : 'ferit123'}

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form['isim']
        password = request.form['pwd']
        if name in users and password == users[name]:
            return render_template('hi.html', name=name)
        else:
            flash("Username or Password is incorrect. Please try again", "warning")
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug = True)