from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import mysql.connector
import sqlite3

from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.secret_key = "super_secret_key_123"

# ---------------- DB CONNECTION ----------------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cybersecurity_awareness"
    )


@app.route("/register")
def register():
    return render_template("registeration.html")

# # ---------------- REGISTER API ----------------
@app.route("/register", methods=["POST"])
def register_db():
    try:
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO users (fullname,  email,  password) VALUES (%s,%s,%s)",
            (fullname,  email,  password)
        )
        db.commit()

        return redirect(url_for('awareness'))

    except Exception as e:
        print("Error:", e)
        return jsonify({"message": "Registration failed"}), 500
   
    finally:
        cursor.close()
        db.close()
        
      
    
# ---------------- LOGIN API ----------------
@app.route("/login")
def login_page():
    return render_template("loginpage.html")

@app.route("/login", methods=["POST"])
def login():
    
    email = request.form.get('email')
    password = request.form.get('password')
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email, password)
    )
    user = cursor.fetchone()

    cursor.close()
    db.close()

    if user:
        session["email"] = user["email"]
        session["password"] = user["password"]
        # return redirect(url_for('awareness'))
        return render_template("loginpage.html", success="Login successful.")
    else:
        
        # return redirect(url_for('register'))
         return render_template("loginpage.html", error="Login failed. Please enter valid details.")
    return render_template("loginpage.html")


# -----------------------------------Quiz API----------------------------------------------------
@app.route("/quiz", methods=["GET", "POST"])
def quiz_db():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    # Fetch all questions
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()

    score = None
    total_questions = len(questions)

    if request.method == "POST":
        score = 0
        user_email = request.form.get("email")  # Add email input in HTML

        for q in questions:
            q_id = str(q['id'])
            selected = request.form.get("q" + q_id)
            if selected and int(selected) == q['correct_option']:
                score += 1

        # Store score in database
        cursor.execute(
            "INSERT INTO user_scores (user_email, score, total_questions) VALUES (%s, %s, %s)",
            (user_email, score, total_questions)
        )
        db.commit()

    cursor.close()
    db.close()

    return render_template("quiz.html", questions=questions, score=score, total_questions=total_questions)

#------------------------------- Dashboard---------------------
@app.route("/dashboard")
def dashboard_db():
    if "user" in session:
        return render_template("dashboard.html", name=session["user"])
    return redirect("/login")

# ---------------- Forget API ----------------
# Forgot Password
@app.route("/forgot", methods=["GET","POST"])
def forgot_db():
    if request.method == "POST":
        email = request.form["email"]
        newpass = request.form["password"]
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("UPDATE users SET password=%s WHERE email=%s",
                       (newpass,email))
        db.commit()
        # return redirect("/login")
        return render_template("forgot.html", success="Password updated successfully.")
    
    return render_template("forgot.html")

# ----------------AI Phishing Detection (Simple Logic)-------------------------
@app.route("/aiphishing", methods=["GET","POST"])
def aiphishing_db():
    result=""
    if request.method=="POST":
        text=request.form["message"]

        suspicious_words=["lottery","winner","click here","urgent","bank","password"]

        if any(word in text.lower() for word in suspicious_words):
            result="⚠️ Phishing Detected!"
        else:
            result="✅ Safe Message"

    return render_template("aiphishing.html",result=result)



@app.route('/')
def home():
    return render_template('index.html')


# ------------------Front Page----------------
@app.route('/awareness')
def awareness():
    return render_template('awareness.html')

@app.route('/cybersecurity')
def cybersecurity():
    return render_template('cybersecurity.html')

@app.route('/attacks')
def attacks():
    return render_template('attacks.html')

@app.route('/phishing')
def phishing():
    return render_template('phishing.html')

@app.route('/safe-browsing')
def safebrowsing():
    return render_template('safe-browsing.html')

@app.route('/social-media')
def socialmedia():
    return render_template('social-media.html')

# ---------------------Attacks Pages------------------

@app.route('/real-attacks')
def realattacks():
    return render_template('real-attacks.html')

@app.route('/Phishing-Attacks')
def Phishingattacks():
    return render_template('Phishing-Attacks.html')

@app.route('/Malware-Attacks')
def Malwareattacks():
    return render_template('Malware-Attacks.html')

@app.route('/Ransomware-Attacks')
def Ransomwareattacks():
    return render_template('Ransomware-Attacks.html')

@app.route('/Dos&Ddos-Attacks')
def Dosattacks():
    return render_template('Dos&Ddos-Attacks.html')

@app.route('/SQL-Attacks')
def sqlattacks():
    return render_template('SQL-Attacks.html')

@app.route('/zero-Attacks')
def zeroattacks():
    return render_template('zero-Attacks.html')

# -------------Quiz Pages----------------------------
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/malware-quiz')
def malwarequiz():
    return render_template('malware-quiz.html')

@app.route('/ransomware-quiz')
def ransomwarequiz():
    return render_template('ransomware-quiz.html')


@app.route('/ddos-quiz')
def ddosquiz():
    return render_template('ddos-quiz.html')


@app.route('/sql-quiz')
def sqlquiz():
    return render_template('sql-quiz.html')

# -----------Home Page-------------------
@app.route('/homepage')
def homepageequiz():
    return render_template('homepage.html')


# -------Forgot Page----------------------------------------
@app.route('/forgot')
def forget():
    return render_template('forgot.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/aiphishing')
def aiphishing():
    return render_template('aiphishing.html')

#--------------------------------Safe Browsing Pages---------------------------------
@app.route('/Unknown-links')
def Unknownlinks():
    return render_template('Unknown-links.html')

@app.route('/Http-website')
def Httpwebsite():
    return render_template('Http-website.html')

@app.route('/Antivirus')
def Antivirus():
    return render_template('Antivirus.html')

@app.route('/Authentication')
def Authentication():
    return render_template('Authentication.html')
# ------------------------------Social Media Pages------------------------------
@app.route('/Strong-pwd')
def Strongpwd():
    return render_template('Strong-pwd.html')

@app.route('/Otp')
def Otp():
    return render_template('Otp.html')

@app.route('/Privacy')
def Privacy():
    return render_template('Privacy.html')

@app.route('/Verify')
def Verify():
    return render_template('Verify.html')
# ------------------------------Real Attacks Pages------------------------------
@app.route('/Big-basket')
def Bigbasket():
    return render_template('Big-basket.html')

@app.route('/Aadhar')
def Aadhar():
    return render_template('Aadhar.html')

@app.route('/Data')
def data_page():
    return render_template('data.html')

@app.route('/Wannacry-attack')
def Wannacryattack():
    return render_template('Wannacry-attack.html')

# --------------------Report page-----------------------------

@app.route('/report')
def report():
    return render_template('report.html')


# ===== Route 1: Report Submission =====
@app.route('/report', methods=['POST'])
def report_db():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reports (name, email, message) VALUES (%s, %s, %s)",
        (name, email, message)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/thank-you')  # Optional thank you page

# ===== Optional Thank You Page =====
@app.route('/thank-you')
def thank_you():
    return "<h2>Thank you for your report! We will review it shortly.</h2>"

# ===== Route 2: Admin Login =====
@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Basic hardcoded check - replace with secure DB check in production
        if username == 'admin' and password == '@admin123':
            session['admin'] = True
            return redirect('/admin')
        else:
            return "Invalid credentials"
    return render_template('admin-login.html')

# ===== Route 3: Admin Page to View Reports =====
@app.route('/admin')
def admin():
    if not session.get('admin'):
        return redirect('/admin-login')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, message, created_at FROM reports ORDER BY created_at DESC")
    reports = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('admin.html', reports=reports)


if __name__ == '__main__':
    app.run(debug=True)
