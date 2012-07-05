from flask import Flask, redirect, url_for, render_template, request
from model import app, Task
import model as m

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return_str = ""
    tasks = Task.query.all()
    return render_template("list_tasks.html", tasks=tasks)

# @app.route("/", methods=["POST"])
# def complete(self,num):
# 	t = m.Task.query.get(num)
# 	t.complete()
# 	m.save_all()
# 	return redirect("/")

@app.route("/add", methods=["GET"])
def make_task():
    return render_template("add.html")

@app.route("/add", methods=["POST"])
def save_task():
	t = m.Task(request.form['title'], notes=request.form['notes'])
	m.add(t)
	m.save_all()
	return redirect("/")

@app.route("/task/<task_id>", methods=["GET"])
def view(task_id):
	t = Task.query.get(task_id)
	print t
	return render_template("task.html", task=t)

@app.route("/task/<task_id>", methods=["POST"])
def update_task(task_id):
	t = m.Task.query.get(task_id)
	t.title = request.form['title']
	t.notes = request.form['notes']
	m.save_all()
	return redirect(url_for("home"))	

@app.route("/task/complete/<task_id>", methods=["POST"])
def complete_task(task_id):
	t = m.Task.query.get(task_id)
	t.complete()
	m.save_all()
	return redirect(url_for("home"))	


if __name__ == '__main__':
    app.run(debug=True)
