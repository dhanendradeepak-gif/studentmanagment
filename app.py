
from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

FILE = "students.json"

# ---------- Load students ----------
def load_students():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# ---------- Save students ----------
def save_students(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

# ---------- Home Page ----------
@app.route("/")
def index():
    students = load_students()
    return render_template("index.html", students=students)

# ---------- Add Student ----------
@app.route("/add", methods=["POST"])
def add_student():
    students = load_students()

    student_id = request.form.get("id")
    name = request.form.get("name")
    age = request.form.get("age")

    if not student_id or not name or not age:
        return "All fields are required", 400

    student = {
        "id": student_id,
        "name": name,
        "age": age
    }

    students.append(student)
    save_students(students)

    return redirect(url_for("index"))

# ---------- Delete Student ----------
@app.route("/delete/<student_id>")
def delete_student(student_id):
    students = load_students()

    students = [
        s for s in students
        if str(s.get("id")) != str(student_id)
    ]

    save_students(students)

    return redirect(url_for("index"))

# ---------- Run App ----------
if __name__ == "__main__":
  import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)