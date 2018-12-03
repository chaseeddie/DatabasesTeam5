from flask import Flask, render_template, redirect, url_for, request
import pymysql

app = Flask(__name__)

#  DATABASE CONFIG #

conn = pymysql.connect(host='localhost', user='root', password='root', db='version1')

cursor = conn.cursor()


@app.route('/purchase_order', methods = ['GET', 'POST'])
def purchase_order():
    if request.method == 'POST':
        PurchSearch = request.form['PurchSearch']
        cursor.execute('SELECT PurchID, PurchaseQuantity FROM PurchaseOrder WHERE PurchID = %s GROUP BY PurchID',(PurchSearch))

        quantity_data = cursor.fetchall()

        conn.commit()

        PurchID = request.form['PurchID']
        PurchQuantity = request.form['PurchQuantity']
        ShippingAddress = request.form['ShippingAddress']
        Payment = request.form['Payment']
        PhoneNum = request.form['PhoneNum']
        SupplierID_1 = request.form['SupplierID_1']
        EmailAddress = request.form['EmailAddress']
        cursor.execute(
            """INSERT INTO PurchaseOrder(PurchID, PurchQuantity, PurchAmount, ShippingAddress, Payment, PhoneNum, SupplierID_1, EmailAddress)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (PurchID, PurchQuantity, PurchAmount, ShippingAddress, Payment, PhoneNum, SupplierID_1, EmailAddress)
        )
        #save data
        conn.commit()
    
    return render_template('purchase_order.html')
    
if __name__ == "__main__":
    app.run(debug=True)

