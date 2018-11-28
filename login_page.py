from flask import Flask, render_template, redirect, url_for, request
import pymysql

app = Flask(__name__)

#  DATABASE CONFIG #

conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='version1')

cursor = conn.cursor()

# this is our homepage

@app.route('/', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        attempted_user = request.form['username']
        attempted_pass = request.form['password']
        result_value = cursor.execute(
            "SELECT * FROM admins WHERE username = %s AND password = %s GROUP BY username",
            (attempted_user, attempted_pass)
        )
         #gets the number of rows affected by the command executed
        if result_value > 0:
        #if attempted_user == 'admin' and attempted_pass == 'admin':

            return redirect(url_for('admin_home'))
        else:
            error = 'Invalid username or password!'
    return render_template('login.html', error= error)

@app.route('/admin_home')
def admin_home():
    return render_template('home.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

if __name__ == "__main__":
    app.run(debug=True)
