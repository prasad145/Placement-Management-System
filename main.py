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

@app.route('/admin_home', methods = ['GET', 'POST'])
def admin_home():
    global cred
    if request.method == 'POST':
        name = request.form['NAME']
        ctc = request.form['CTC']
        role = request.form['ROLE']
        cgpa = request.form['CGPA']
        backs = request.form['BACKS']
        with sqlite3.connect("data.db") as conn:
            curr = conn.cursor()
            curr.execute("INSERT INTO companyDB(company_name, CTC, offered_Role, CGPA, backs) values( company_name =:company_name, CTC =: CTC, offered_Role =: offered_role, CGPA =:CGPA, backs =: backs",{"company_name" : name, "CTC" : ctc, "offered_Role" : role, "CGPA" : cgpa, "backs" : backs})
            conn.commit()
    else:    
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
                    flash('Wrong')
                    return render_template('login.html',)

    else:
        return render_template("login.html")

@app.route('/company/<int:companyID>')
def dispCompany(companyID):
    companyData = None
    return render_template('company.html', data = companyData)

if __name__ == '__main__':
    app.secret_key = "#weareallnerds69"
    app.run(debug = True)