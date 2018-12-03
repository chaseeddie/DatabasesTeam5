from flask import Flask, render_template, redirect, url_for, request
import pymysql

app = Flask(__name__)

#  DATABASE CONFIG #

conn = pymysql.connect(host='localhost', user='root', password='root', db='version1')

cursor = conn.cursor()

@app.route('/order_receipt')
def order_receipt():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM OrderReceipt')
    receipt_data = cursor.fetchall()

    return render_template('order_receipt.html', data=receipt_data)

if __name__ == "__main__":
    app.run(debug=True)

