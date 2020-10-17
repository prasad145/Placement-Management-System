import sqlite3
from flask import Flask , render_template , redirect , url_for , request , session
from flask_sqlalchemy import SQLAlchemy

cred = []
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

#db = SQLAlchemy(app)


@app.route("/")
def m():
    return redirect('/login')

@app.route('/home')
def home():
    global cred
    return (render_template('home.html', data = cred))

@app.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')

@app.route('/login', methods = ['GET','POST'])
def logi():
    global cred
    if request.method == 'POST':      
        id = request.form['USN']
        password = request.form['PW']
      #  credentials = studentDB.query.get(id)
        with sqlite3.connect("data.db") as con:
            cur = con.cursor()
            cred = cur.execute("SELECT * FROM studentDB where usn = :usn", {"usn" : id}).fetchone() 
        
            if cred is None:
                return render_template('login.html')
            else:
                if cred[2] == password:
                    return redirect('/home')
                else:
                    return render_template('login.html',)

    else:
        return render_template("login.html")

if __name__ == '__main__':
    app.secret_key = "#weareallnerds69"
    app.run(debug = True)
