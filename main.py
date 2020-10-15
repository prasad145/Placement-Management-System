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
def admin_home():
    return render_template('admin_home.html')

@app.route('/login', methods = ['GET','POST'])
def logi():
    if request.method == 'POST':
        id = request.form.get("USN")
        password = request.form.get("PW")
        #secure_pass = sha256_crypt.encrypt(str(password))
        #db.execute("""ALTER TABLE students 
        #            ADD secretkey varchar(40) WHERE usn = :usn""",{"usn" : id})
        #db.execute("""INSERT INTO students
          #            (secretkey) values(:secretkey)""",{"secretkey" : secure_pass})
        usernamedata = db.execute("SELECT usn FROM student where usn = :usn",{"usn" : id}).fetchone()   
        passworddata = db.execute("SELECT usn from student where first_name = :first_name",{"first_name" : password}).fetchone()

        if usernamedata is None:
            #put flash messege here
            return render_template("login.html")
        else:
            if passworddata is not None: 
            #for password_data in passworddata:
             #   if sha256_crypt.verify(password, password_data):
                    #put flash messege here ("login successfull")
                return redirect(url_for('register'))
            else:
                #put flash messege ("incorrect password")
                return render_template("login.html")

        db.commit()         

if __name__ == '__main__':
    app.secret_key = "#weareallnerds69"
    app.run(debug = True)
