from flask import Flask, request, render_template, redirect, flash, make_response, session, escape, url_for

app = Flask(__name__)
app.secret_key = 'secret'

users = {'burak':'burak123', 'berk':'berk123', 'cenk':'cenkalti', 'ferit':'ferit123'}

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form['isim']
        password = request.form['pwd']
        if name in users and password == users[name]:
            session['name'] = name
            return redirect(url_for('hello_world'))
        else:
            flash("Username or Password is incorrect."
                  " Please try again", "warning")
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('name', None)
    return redirect(url_for('hello_world'))


@app.route('/session')
def dump_session():
    response = make_response(repr(session))
    response.content_type = 'text/plain'
    return response

if __name__ == '__main__':
    app.run(debug = True)