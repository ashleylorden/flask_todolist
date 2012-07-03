from flask import Flask, redirect, url_for, render_template, request
from model import app, Task
import model as m

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return_str = ""
    tasks = Task.query.all()
    return render_template("list_tasks.html", tasks=tasks)

@app.route("/", methods=["POST"])
def complete(self,num):
	t = m.Task.query.get(num)
	t.complete()
	m.save_all()
	return redirect("/")

@app.route("/add", methods=["GET"])
def make_task():
    return render_template("add.html")

@app.route("/add", methods=["POST"])
def save_task():
	print request.form
	t = m.Task(request.form['title'], notes=request.form['notes'])
	m.add(t)
	m.save_all()
	return redirect("/")
	

if __name__ == '__main__':
    app.run(debug=True)