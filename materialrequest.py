from flask import Flask, render_template, redirect, url_for, request
import pymysql

app = Flask(__name__)

#  DATABASE CONFIG #

conn = pymysql.connect(host='localhost', user='root', password='root', db='version1')

cursor = conn.cursor()



@app.route('/materialrequest', methods=['GET', 'POST'])
def vendors():
    if request.method == 'POST':
        itemcode = request.form['itemcode']
        itemname = request.form['itemname']
        description = request.form['description']
        price = request.form['price']
        manufacturedate = request.form['manufacturedate']
        expiredate = request.form['expiredate']
        manufacturer = request.form['manufacturer']
        supplier = request.form['supplier']
        cursor.execute(
            """INSERT INTO Vendors(itemcode, itemname, description, price, manufacturedate, expiredate, manufacturer, supplier)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (itemcode, itemname, description, price, manufacturedate, expiredate, manufacturer, supplier)
        )
        conn.commit()

        return render_template('materialrequest.html')
    return render_template('materialrequest.html')