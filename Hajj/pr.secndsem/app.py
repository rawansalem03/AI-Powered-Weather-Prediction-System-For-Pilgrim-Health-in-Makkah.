from flask import Flask, send_from_directory 

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def home():
    return send_from_directory(".", "employee_dashboard.html")

@app.route("/<path:path>")
def files(path):
    return send_from_directory(".", path)from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def home():
    return send_from_directory(".", "employee_dashboard.html")

@app.route("/<path:path>")
def files(path):
    return send_from_directory(".", path)
