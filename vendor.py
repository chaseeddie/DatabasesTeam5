from flask import Flask, render_template, redirect, url_for, request
import pymysql

app = Flask(__name__)

#  DATABASE CONFIG #

conn = pymysql.connect(host='localhost', user='root', password='root', db='version1')

cursor = conn.cursor()



@app.route('/vendors', methods=['GET', 'POST'])
def vendors():
    if request.method == 'POST':
        vendorid = request.form['vendorID']
        venName = request.form['VenName']
        minorquantity = request.form['MinOrdQuantity']
        quality = request.form['quality']
        emailaddress = request.form['emailaddress']
        phonenum = request.form['phonenum']
        cursor.execute(
            """INSERT INTO Vendors(VendorID, VenName, MinOrdQuantity, Quality, EmailAddress, PhoneNum)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (vendorid, venName, minorquantity, quality, emailaddress, phonenum)
        )
        conn.commit()

        return render_template('registration_test.html')
    return render_template('registration_test.html')