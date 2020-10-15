from student_class import Student
from flask import Flask , render_template , redirect , url_for , request , session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from passlib.hash import sha256_crypt

engine = create_engine("sqlite:///std_data.db", echo = True)

db = scoped_session(sessionmaker(bind = engine))

app = Flask(__name__)

@app.route("/")
def m():
    return redirect('/login')

@app.route('/home')
def home():
    return (render_template('login.html'))

@app.route('/admin_home')
def adminHome():
    return render_template('admin_home.html')

@app.route('/login', methods = ['GET','POST'])

def studentLogin():
    return render_template('login.html')

def logi():
    if request.method == 'POST':
        id =  str(input())                     #request.form.get("id")
        password = str(input())                 #request.form.get("password")
        secure_pass = sha256_crypt.encrypt(str(password))
        db.execute("""ALTER TABLE students 
                     ADD secretkey varchar(40)""")
        db.execute("""INSERT INTO students
                      (secretkey) values(:secretkey)""",{"secretkey" : secure_pass})
        usernamedata = db.execute("SELECT usn FROM students where usn = :usn",{"usn" : id}).fetchone()   
        passworddata = db.execute("SELECT secretkey from students where usn = :usn",{"usn" : id}).fetchone()

        if usernamedata is None:
            #put flash messege here
            return render_template("login.html")
        else: 
            for password_data in passworddata:
                if sha256_crypt.verify(password, password_data):
                    #put flash messege here ("login successfull")
                    return redirect(url_for('register'))
                else:
                    #put flash messege ("incorrect password")
                    return render_template("login.html")

        db.commit()          
    


"""
im no longer verifying the user credential through this
>>>>>>> c5352dc12c0012b958ea1dd90df1dc1f80cf0b86

@app.route('/adminlogin')
def adminLogin():
    return (render_template('login_admin.html'))

def login():
    error = None
    if request.method == 'POST':
        if (request.form['username'] != 'admin' and request.form['username'] != 'student') or request.form['password'] != 'admin' :
            error = "Invalid credentials, Please try again!."
        elif request.form['username'] == 'admin':
            return redirect(url_for('admin_home'))
        elif request.form['username'] == 'student':
            return redirect(url_for('home'))

    return render_template('login.html', error = error)
"""

if __name__ == '__main__':
   # path = "data.xlsx"
   # cur = xlrd.open_workbook(path)
   
   # first_sheet = cur.sheet_by_index(0)
   # print(first_sheet.row_values(0))
    app.secret_key = "#weareallnerds69"
    app.run(debug = True)
