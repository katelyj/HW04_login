from flask import Flask, render_template, request
import hashlib
import csv

ramirez = Flask(__name__)

def hash(s):
    p = hashlib.sha1()
    p.update(s)
    return p.hexdigest()

def register(user,password):
    data = csv.reader(open("data/d.csv"))
    for i in data:
	if user == i[0]:
		return "Ya registered already, punk!"
    with open('data/d.csv', 'a') as f:
	w = csv.writer(f)
	w.writerow([user,hash(password)])
    return "Congrats! You can now log in..."

def check(user,password):
    data = csv.reader(open("data/d.csv"))
    for i in data:
	if user == i[0]:
	    if i[1] == hash(password):
		return "Success!"
	return "You went wrong there, hun."
    return "Have you even registered?"

@ramirez.route("/")
@ramirez.route("/login/")
def home():
    return render_template("form.html")

@ramirez.route("/authenticate/", methods=['GET','POST'])
def auth():
    inp = request.form
    user = inp['user']
    password = inp['password']
    if inp['s'] == "Register":
	m = register(user,password)
    else:
        m = check(user,password)
    return render_template("results.html",result=m)

if __name__ == '__main__':
    ramirez.debug = True
    ramirez.run()
