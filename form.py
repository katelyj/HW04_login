from flask import Flask, render_template, request

ramirez = Flask(__name__)

@ramirez.route("/")
@ramirez.route("/login/")
def home():
    print request.headers
    return render_template("form.html")

@ramirez.route("/authenticate/", methods=['GET','POST'])
def auth():
    print request.form
    print request.form["user"]
    print request.form["password"]
    return "ok then"

if __name__ == '__main__':
    ramirez.debug = True
    ramirez.run()
