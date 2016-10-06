from flask import Flask, render_template, request, session, url_for
import hashlib
import csv

ramirez = Flask(__name__)
ramirez.secret_key = "\xceY\x96\x0b^\x8d:\xea\xd2\x9c\xae\xf2\xfc\xdd\x8dL\xf5Dsw\x8a\xcb=\xf8\xf1\xe5\x89K\xbd\x17\x1eg"

def hash(s):
    p = hashlib.sha1()
    p.update(s)
    return p.hexdigest()

def register(user,password):
    DATA = csv.reader(open("data/d.csv"))
    for i in DATA:
	if user == i[0]:
		return "Ya registered already, punk!"
    with open('data/d.csv', 'a') as f:
	w = csv.writer(f)
	w.writerow([user,hash(password)])
    return "Congrats! You can now log in..."

def check(user,password):
    DATA = csv.reader(open("data/d.csv"))
    for i in DATA:
	if user == i[0]:
	    if i[1] == hash(password):
		return "Success!"
	    return "You went wrong there, hun."
    return "Have you even registered?"

@ramirez.route("/")
@ramirez.route("/login/")
def home():
    #print request headers
    print url_for('home')
    print url_for('auth')
    return render_template("form.html",result="Write whatever comes to your heart...")

@ramirez.route("/authenticate/", methods=['GET','POST'])
def auth():
    inp = request.form
    user = inp['user']
    password = inp['password']
    if inp['s'] == "Register":
	m = register(user,password)
    else:
        m = check(user,password)
    return render_template("form.html",result=m)

if __name__ == '__main__':
    ramirez.debug = True
    ramirez.run()
