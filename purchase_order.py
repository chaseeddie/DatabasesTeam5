from flask import Flask, render_template, redirect, url_for, request
import pymysql

app = Flask(__name__)

#  DATABASE CONFIG #

conn = pymysql.connect(host='localhost', user='root', password='root', db='version1')

cursor = conn.cursor()

cursor.execute('SELECT * FROM PurchaseOrder WHERE PurchQuantity = %s GROUP BY PurchID')
quantity_data = cursor.fetchall()

conn.commit()

@app.route('/purchase_order', methods = ['GET', 'POST'])
def purchase_order():
    if request.method == 'POST':
        PurchID = request.form['PurchID']
        PurchQuantity = request.form['PurchQuantity']
        ShippingAddress = request.form['ShippingAddress']
        Payment = request.form['Payment']
        PhoneNum = request.form['PhoneNum']
        SupplierID_1 = request.form['SupplierID_1']
        Email Address = request.form['Email Address']
        cursor.execute(
            """INSERT INTO PurchaseOrder(PurchID, PurchQuantity, PurchAmount, ShippingAddress, Payment, PhoneNum, SupplierID_1, Email Address)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (PurchID, PurchQuantity, PurchAmount, ShippingAddress, Payment, PhoneNum, SupplierID_1, Email Address)
        )
        #save data
        conn.commit()
    
    return render_template('purchase_order.html')
    
if __name__ == "__main__":
    app.run(debug=True)
