from flask import Flask, render_template, request

ramirez = Flask(__name__)

@ramirez.route("/")
@ramirez.route("/login/")
def home():
    return render_template("form.html")

@ramirez.route("/authenticate/", methods=['GET','POST'])
def auth():
    correctU = "monsieur"
    correctP = "ramirez"
    if request.form["user"] == correctU and request.form["password"] == correctP:
        m = "SUCCESS!!!"
    else:
        m = "FAILURE!!!"
    return render_template("results.html",result=m)

if __name__ == '__main__':
    ramirez.debug = True
    ramirez.run()
