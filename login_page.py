from flask import Flask, render_template, redirect, url_for, request
import pymysql

app = Flask(__name__)

#  DATABASE CONFIG #

conn = pymysql.connect(host='localhost', user='root', password='root', db='version1')

cursor = conn.cursor()


# LOGIN PAGE

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        attempted_user = request.form['username']
        attempted_pass = request.form['password']

        # QUERIES TO CHECK ROLES

        result_value = cursor.execute(
            "SELECT * FROM user_info WHERE BINARY username = %s AND BINARY password = %s GROUP BY username",
            (attempted_user, attempted_pass)
        )
        result_admin = cursor.execute(
            """SELECT * FROM user_info WHERE BINARY username = %s AND 
            BINARY password = %s AND role = %s GROUP BY username""",
            (attempted_user, attempted_pass, 'admin')
        )
        result_manager = cursor.execute(
            """SELECT * FROM user_info WHERE BINARY username = %s AND 
            BINARY password = %s AND role = %s GROUP BY username""",
            (attempted_user, attempted_pass, 'manager')
        )
        result_vendor = cursor.execute(
            """SELECT * FROM user_info WHERE BINARY username = %s AND 
            BINARY password = %s AND role = %s GROUP BY username""",
            (attempted_user, attempted_pass, 'vendor')
        )
        # gets the number of rows affected by the command executed
        if result_value > 0:
            if result_admin > 0:
                return redirect(url_for('admin_home'))
            elif result_manager > 0:
                return redirect(url_for('manager_home'))
            elif result_vendor > 0:
                return redirect(url_for('vendor_home'))
            else:
                return redirect(url_for('floor_home'))
        else:
            error = 'Invalid username or password!'
    return render_template('login.html', error=error)


@app.route('/vendor_home', methods=['GET', 'POST'])
def vendor_home():
    return render_template('home_vendor.html')

@app.route('/manage_materials', methods=['GET', 'POST'])
def manage_materials():
    if request.method == 'POST':
        itemCode = request.form['itemCode']
        itemName = request.form['itemName']
        itemQt = request.form['itemQt']
        itemDescription = request.form['itemDescription']
        itemPrice = request.form['itemPrice']
        itemSupplier = request.form['itemSupplier']
        itemDateMan = request.form['itemDateMan']
        itemExpDate = request.form['itemExpDate']
        itemImage = request.form['itemImage']
        cursor.execute(
            """INSERT INTO items(code, name, quantity, description, price, supplier, 
            dateManufactured, expirationDate, image)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (itemCode, itemName, itemQt, itemDescription, itemPrice, itemSupplier, itemDateMan,
             itemExpDate, itemImage)
        )
        conn.commit()
        return render_template('manage_materials.html')
    return render_template('manage_materials.html')

@app.route('/manager_home', methods=['GET', 'POST'])
def manager_home():
    return render_template('home_manager.html')

@app.route('/manage_vendor', methods=['GET', 'POST'])
def manage_vendor():
    if request.method == 'POST':

        venName = request.form['venName']
        minorquantity = request.form['minOrdQuantity']
        datepurchased = request.form['datePurchased']
        itempurchased = request.form['itemPurchased']
        quality = request.form['quality']
        emailaddress = request.form['emailaddress']
        phonenum = request.form['phonenum']

        cursor.execute(
            """INSERT INTO vendors(VenName, MinOrdQuantity, DatePurchased, ItemsPurchased, 
            Quality, EmailAddress, PhoneNum)
            VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            (venName, minorquantity, datepurchased, itempurchased,
             quality, emailaddress, phonenum)
        )
        conn.commit()

        return render_template('manage_vendor.html')
    return render_template('manage_vendor.html')



@app.route('/floor_home')
def floor_home():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user_info')
    floor_data = cursor.fetchall()

    return render_template('home_shopfloor.html', data=floor_data)



@app.route('/admin_home')
def admin_home():
    return render_template('home_admin.html')

@app.route('/shipping_details', methods = ['GET','POST'])
def shipping_details():
    if request.method == 'POST':
        shipAddress = request.form['shipAddress']
        contactEmail = request.form['contactEmail']
        contactPhone = request.form['contactPhone']
        paymentMethod = request.form['paymentMethod']

        cursor.execute(
            """INSERT INTO shippingdetails(shipAddress, contactEmail, contactPhone, paymentMethod)
            VALUES (%s, %s, %s, %s)""",
            (shipAddress, contactEmail, contactPhone, paymentMethod)
        )
        conn.commit()

        return redirect(url_for('shipping_details'))

    return render_template('admin_shipping_details.html')


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

        return redirect(url_for('registration'))
    return render_template('registration.html')


if __name__ == "__main__":
    app.run(debug=True)
