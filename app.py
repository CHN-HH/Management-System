from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = "case.db"

# 初始化数据库
def init_db():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS patient_case (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        id_card TEXT,
        diagnose TEXT,
        symptom TEXT,
        treatment TEXT,
        create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

# 获取数据库连接
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    db = get_db()
    cases = db.execute("SELECT * FROM patient_case ORDER BY create_time DESC").fetchall()
    db.close()
    return render_template("index.html", cases=cases)

@app.route("/add", methods=["GET","POST"])
def add_case():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        id_card = request.form["id_card"]
        diagnose = request.form["diagnose"]
        symptom = request.form["symptom"]
        treatment = request.form["treatment"]
        db = get_db()
        db.execute('''
        INSERT INTO patient_case(name,age,gender,id_card,diagnose,symptom,treatment)
        VALUES (?,?,?,?,?,?,?)
        ''',(name,age,gender,id_card,diagnose,symptom,treatment))
        db.commit()
        db.close()
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/detail/<int:cid>")
def case_detail(cid):
    db = get_db()
    item = db.execute("SELECT * FROM patient_case WHERE id=?",(cid,)).fetchone()
    db.close()
    return render_template("detail.html",item=item)

@app.route("/delete/<int:cid>")
def delete_case(cid):
    db = get_db()
    db.execute("DELETE FROM patient_case WHERE id=?",(cid,))
    db.commit()
    db.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
