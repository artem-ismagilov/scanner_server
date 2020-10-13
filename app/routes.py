from app import app
from flask import render_template
import socket
import os


PATH = "/Users/artem_ismagilov/Desktop/static"


@app.route('/')
def index():
    print("Showing", app.config["LAST_PHOTO"])
    pic = []
    try:
        pic = os.listdir("/Users/artem_ismagilov/Documents/server/app/static/" + app.config["LAST_PHOTO"])
    except:
        print("No such directory")
        app.config["LAST_PHOTO"] = "no_data"

    print(pic)
    return render_template("index.html", dir=app.config["LAST_PHOTO"], pictures=pic)


@app.route('/scan')
def scan():
    try:
        app.config["LAST_PHOTO"] = "no_data"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), 1234))
        s.send(b'SCAN')
        s.close()
    except:
        print("Error during sending message")

    return render_template("scan.html")
