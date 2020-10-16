from student_class import Student
import sqlite3
from flask import Flask , render_template , redirect , url_for , request , session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from passlib.hash import sha256_crypt

#engine = create_engine("sqlite:///data.db", echo = True)

#db = scoped_session(sessionmaker(bind = engine))

db = sqlite3.connect('data.db')
cur = db.cursor()

app = Flask(__name__)


@app.route("/")
def m():
    return redirect('/login')

@app.route('/home')
def home():
    return (render_template('login.html'))

@app.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')

@app.route('/login', methods = ['GET','POST'])
def logi():
    if request.method == 'POST':
        id = request.form.get("USN")
        password = request.form.get("PW")
        
        usernamedata = cur.execute("SELECT * FROM studentDB where usn = :usn",{"usn" : id}).fetchone()
        if usernamedata is None:
            return render_template('login.html')
        else:
            if (usernamedata[2] == password):
                return render_template('home.html')
            else:
                pass
        # passworddata = cur.execute("SELECT usn from studentDB where fname = :fname",{"fname" : password}).fetchone()

    else:
        return render_template("login.html")

                 

if __name__ == '__main__':
    app.secret_key = "#weareallnerds69"
    app.run(debug = True)
