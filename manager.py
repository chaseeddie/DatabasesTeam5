from flask import Flask, render_template, redirect, url_for, request
from pymysql import cursors
import pymysql

app = Flask(__name__)

#connect to your database with your own password, etc.
conn = pymysql.connect(host='localhost', user='root', password='password', db='version1')

cursor = conn.cursor()

cursor.execute

@app.route('/', methods = ['POST','GET'])
def manageitems():
    if request.method == 'POST':
        itemID = request.form['itemID']
        itemName = request.form['itemName']
        quantity = request.form['quantity']
        description = request.form['description']
        price = request.form['price']
        manufactor = request.form['manufactor']
        manufacDate = request.form['manufacDate']
        expireDate = request.form['expireDate']
        itemImage = request.form['itemImage']
 
        cursor.execute(
            """INSERT INTO Items (ItemID, ItemName, Quantity, itemDesc, Price, Manufactorer, ManufacDate, ExpireDate, ItemImage)
            VALUES (%s, %s, %s ,%s ,%s ,%s ,%s ,%s, %s)"""
            (itemID, itemName, description, price, manufacDate, expireDate, manufactor, supplier)           
        )
        
        #save changes
        conn.commit()
         
    return render_template('manage.html')


@app.route('/managevendors')
def managevendors():
    return render_template('vendors.html')

@app.route('/materialrequest')
def materialrequest():
    return render_template('request.html')

if __name__ == "__main__":
    app.run(debug=True)
    
conn = close()
