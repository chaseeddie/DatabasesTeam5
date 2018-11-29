from flask import Flask, render_template

app = Flask(__name__)

db = pymysql.connect(host='localhost', user='root', password='password', db='version1')


@app.route("/")
def manage():
    return render_template("manage.html")

@app.route("/vendors")
def vendors():
    return render_template("vendors.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

