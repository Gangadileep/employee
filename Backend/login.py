from crypt import methods
from sqlite3 import Cursor
from ssl import SSLSession
import pymysql
from app import app
from config import mydb
from flask import jsonify,redirect,session,url_for
from flask import flash, request,render_template



@app.route("/")
def index():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template("project.html", username= session['username'])




@app.route('/login' , methods=['GET','POST'])
def login():
    
    if request.method=='POST':
        conn = mydb.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM user WHERE username=%s and password=%s',(username,password))
        record= cursor.fetchone()
        if record:
            session['loggedin']=True
            session['username']=record[1]
            return redirect(url_for('project'))
        else:
            msg ="incorect user name or p"
    return render_template('login.html', msg=msg)