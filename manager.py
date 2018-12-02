from flask import Flask, render_template, redirect, url_for, request
from pymysql import cursors
import pymysql

app = Flask(__name__)

#connect to your database with your own password, etc.
conn = pymysql.connect(host='localhost', user='root', password='password', db='version1')

cursor = conn.cursor()

cursor.execute

@app.route('/', methods = ['POST','GET'])
def manage():
    if request.method == 'POST':
        itemCode = request.form['itemCode']
        itemName = request.form['itemName']
        description = request.form['description']
        price = request.form['price']
        manufacDate = request.form['manufacDate']
        expireDate = request.form['expireDate']
        manufactor = request.form['manufactor']
        supplier = request.form['supplier']
 
        cursor.execute(
            """INSERT INTO Materials (itemCode, itemName, description, price, manufacDate, expireDate, manufactorer, supplier)
            VALUES (%s, %s, %s ,%s ,%s ,%s ,%s ,%s)"""
            (itemCode, itemName, description, price, manufacDate, expireDate, manufactor, supplier)           
        )
        
        #save changes
        conn.commit()
         
    return render_template('manage.html')


@app.route('/vendors')
def vendors():
    return render_template('vendors.html')

if __name__ == "__main__":
    app.run(debug=True)
    
conn = close()
