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
    with sqlite3.connect("companyDB.db") as conn:
        curr = conn.cursor()
        c_data = curr.execute('SELECT * FROM companies;').fetchall()
    return (render_template('home.html', data = cred, companies = c_data[::-1]))

@app.route('/admin', methods = ['GET', 'POST'])
def admin_home():
    with sqlite3.connect("companyDB.db") as conn:
        curr = conn.cursor()
        c_data = curr.execute('SELECT * FROM companies;').fetchall()
    return render_template('admin_home.html', companies = c_data)

@app.route('/login', methods = ['GET','POST'])
def logi():
    global cred
    if request.method == 'POST':      
        id = request.form['USN']
        password = request.form['PW']
      #  credentials = studentDB.query.get(id)
        with sqlite3.connect("data.db") as con:
            cur = con.cursor()
            cred = cur.execute("SELECT * FROM studentDB where usn = :usn;", {"usn" : id}).fetchone() 
        
            if cred is None:
                return render_template('login.html', invalid = False)
            else:
                if cred[2] == password:
                    return redirect('/home')
                else:
                    # flash('Wrong')
                    return render_template('login.html', invalid = False)

    else:
        return render_template("login.html", invalid = True)

@app.route('/adminlogin', methods = ['GET', 'POST'])
def adminLogin():
    if request.method == 'POST':
        name = request.form["username"]
        pw = request.form['pw']
        print(name, pw)
        if(name == 'admin' and pw == 'admin'):
            return redirect('/admin')
        else:
            return render_template('login_admin.html', invalid = False)
    else:
        return render_template('login_admin.html', invalid = True)


@app.route('/company/<int:companyID>')
def dispCompany(companyID):
    with sqlite3.connect("companyDB.db") as conn:
        curr = conn.cursor()
        q = "SELECT * FROM companies where ID=" + str(companyID) + ";"
        companyData = curr.execute(q).fetchone()
    return render_template('company.html', data = companyData)

@app.route('/new', methods = ['POST', 'GET'])
def addnew():
    if request.method == 'POST':
        name = request.form['name']
        ctc = request.form['CTC']
        role = request.form['role']
        cgpa = request.form['cgpa']
        backs = request.form['backs']
        with sqlite3.connect("companyDB.db") as conn:
            curr = conn.cursor()
            q = "INSERT INTO companies (Name, Role, CCTC, MinCGPA, Backs) values ('" + name +"', '" + role + "'," + ctc + ", " + cgpa +", " + backs + ");"
            curr.execute(q)
            # print(q)
            conn.commit()
        return redirect('/admin')
    else:
        return render_template('add_new.html')

@app.route('/drop/<int:companyID>')
def drop(companyID):
    with sqlite3.connect("companyDB.db") as conn:
        curr = conn.cursor()
        curr.execute("DELETE FROM companies WHERE ID = :del;", { "del" : companyID })
        conn.commit()
    return redirect('/admin')

if __name__ == '__main__':
    app.secret_key = "#weareallnerds69"
    app.run(debug = True)