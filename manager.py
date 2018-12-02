from flask import Flask, render_template
from pymysql import cursors
import pymysql

app = Flask(__name__)

db = pymysql.connect(host='localhost', user='root', password='password', db='version1')

cursor = db.cursor()

@app.route("/")
def manage():
    return render_template("manage.html")

@app.route("/vendors")
def vendors():
    return render_template("vendors.html")

@app.route("/request")
def request():
    return render_template("request.html")

if __name__ == "__main__":
    app.run(debug=True)
