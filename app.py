from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "\xc6\xb0\x8b\xbfl6\xe1k\xb5\x01\xcd\xc3\x1c\xd7\x02\x98"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/project/1")
def project_one():
    return render_template("project_1.html")


if __name__ == "__main__":
	app.run(debug=True)