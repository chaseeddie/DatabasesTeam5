from flask import Flask, render_template, redirect, url_for, request
import pymysql

app = Flask(__name__)

#  DATABASE CONFIG #

conn = pymysql.connect(host='localhost', user='root', password='root', db='version1')

cursor = conn.cursor()


# this is our homepage

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        attempted_user = request.form['username']
        attempted_pass = request.form['password']
        result_value = cursor.execute(
            "SELECT * FROM admins WHERE BINARY username = %s AND BINARY password = %s GROUP BY username",
            (attempted_user, attempted_pass)
        )
        # gets the number of rows affected by the command executed
        if result_value > 0:
            # if attempted_user == 'admin' and attempted_pass == 'admin':

            return redirect(url_for('admin_home'))
        else:
            error = 'Invalid username or password!'
    return render_template('login.html', error=error)


@app.route('/admin_home')
def admin_home():
    return render_template('home.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        r_username = request.form['reg_username']
        r_password = request.form['reg_password']
        r_role = request.form['reg_role']
        r_fname = request.form['reg_fname']
        r_lname = request.form['reg_lname']
        r_email = request.form['reg_email']
        r_phone = request.form['reg_phone']
        r_gender = request.form['reg_gender']
        cursor.execute(
            """INSERT INTO user_info(username, password, role, firstname, lastname, email, phone, gender)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (r_username, r_password, r_role, r_fname, r_lname, r_email, r_phone, r_gender)
        )
        conn.commit()

        return render_template('registration_test.html')
    return render_template('registration_test.html')


if __name__ == "__main__":
    app.run(debug=True)
