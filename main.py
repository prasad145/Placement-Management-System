from flask import Flask , render_template , redirect , url_for , request
import xlrd

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

@app.route('/adminlogin')
def adminLogin():
    return (render_template('login_admin.html'))

def login():
    error = None
    admin_authorised = False
    student_authorised = False
    if request.method == 'POST':
        if (request.form['username'] != 'admin' and request.form['username'] != 'student') or request.form['password'] != 'admin' :
            error = "Invalid credentials, Please try again!."
        elif request.form['username'] == 'admin':
            admin_authorised = True
            return redirect(url_for('admin_home'))
        elif request.form['username'] == 'student':
            student_authorised = True
            return redirect(url_for('home'))

    return render_template('login.html', error = error)

if __name__ == '__main__':
   # path = "data.xlsx"
   # cur = xlrd.open_workbook(path)
   
   # first_sheet = cur.sheet_by_index(0)
   # print(first_sheet.row_values(0))

    app.run(debug = True)
