from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/student")
def student():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT cgpa, status FROM evaluation WHERE student_id = 1")
    result = cur.fetchone()
    return render_template("student.html", cgpa=result[0], status=result[1])

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/evaluate")
def evaluate():
    # Dummy evaluation logic
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("UPDATE evaluation SET status = 'Good Standing' WHERE cgpa >= 6.0")
    con.commit()
    return "Evaluation Done!"

if __name__ == "__main__":
    app.run(debug=True)
