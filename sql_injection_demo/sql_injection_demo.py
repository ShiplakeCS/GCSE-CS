from flask import Flask, g, request, render_template, session, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'sql_injection_demo.db'

app.config['DATABASE'] = DATABASE
app.config['SECRET_KEY'] = "12398yqwleknjs e8yw e;oqi2elkasjo;lal/bl iufgqh2o;w49toi;   j1;q3.a,wsnm.szzd"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        # do login

        sql = 'SELECT * FROM "user" where username="{}" and password="{}"'.format(request.form['username'], request.form['password'])
        print("SQL query processed: {}".format(sql))
        result = get_db().execute(sql).fetchone()

        if result:
            session['activeUser'] = result['username']
            return redirect(url_for("index"))
        else:
            return render_template("login.html", loginFail=True)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    del session['activeUser']
    return redirect(url_for("login"))

@app.route("/")
def index():
    if 'activeUser' not in session:
        return redirect(url_for("login"))
    else:
        return render_template("index.html", user=session['activeUser'])


app.run(host='0.0.0.0', debug=True)