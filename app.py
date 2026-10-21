
from flask import Flask, render_template, request, redirect, url_for
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

students = []
next_id = 1

REQUEST_COUNT = Counter(
    "student_app_requests_total",
    "Total HTTP requests received by the student application"
)

@app.before_request
def count_request():
    REQUEST_COUNT.inc()

@app.route("/")
def home():
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    global next_id

    name = request.form.get("name", "").strip()
    course = request.form.get("course", "").strip()

    if name and course:
        students.append({
            "id": next_id,
            "name": name,
            "course": course
        })
        next_id += 1

    return redirect(url_for("home"))

@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    global students
    students = [
        student for student in students
        if student["id"] != student_id
    ]
    return redirect(url_for("home"))

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
