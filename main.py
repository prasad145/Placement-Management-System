import sqlite3
from flask import Flask , render_template , redirect , url_for , request , session, flash
from flask_sqlalchemy import SQLAlchemy

cred = []
app = Flask(__name__)

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
                flash("Incorrect, Password!!!")
                return render_template('login.html')
            else:
                if cred[2] == password:
<<<<<<< HEAD
                    #comapny database
                    flash("Incorrect, Password!!!")
                    return render_template('home.html')
                else:
                    flash("Incorrect, Password!!!")
                    return render_template('login.html')
=======
                    return redirect('/home')
                else:
                    flash('Wrong')
                    return render_template('login.html',)
>>>>>>> ca3e31896ea3c52923078deb7c3cbbdd3108050d

    else:
        flash("Incorrect, Password!!!")
        return render_template("login.html")

@app.route('/company/<int:companyID>')
def dispCompany(companyID):
    companyData = None
    return render_template('company.html', data = companyData)

if __name__ == '__main__':
    app.secret_key = "#weareallnerds69"
    app.run(debug = True)
