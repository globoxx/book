import os
from tools.interface import *
from tools.parser import *
from tools.encryption import *
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_session import Session
import redis
import hashlib
import pdb

#Attention pour avoir les bonnes versions des librairies voici le site :https://testdriven.io/blog/flask-server-side-sessions/ 
#Pour bien lancer le serveur il faut installer redis et 
#le lancer avec redis-server puis lancer le code python, j'aurais pu le faire directement dans le code mais comme il est destiné à être sur un 
#serveur cela ne fonctionnera pas tout le temps
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', default='BAD_SECRET_KEY')
# Configure Redis for storing the session data on the server-side
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = redis.from_url('redis://127.0.0.1:6379')

# Create and initialize the Flask-Session object AFTER `app` has been configured
server_session = Session(app)

results_sheet = []
detectedFile = []
path = os.path.join(os.getcwd(), "files")

def refresh_files():
    global detectedFile, path
    detectedFile = [file for file in os.listdir() if file.endswith(".sm")]
    if os.path.exists(path) and os.path.isdir(path):
        detectedFile = [file for file in os.listdir(path) if file.endswith(".sm")]
    else:
        os.makedirs(path)
        detectedFile = []

@app.route("/")
def index():
    refresh_files()
    return render_template("index.html", detectedFile=detectedFile)

@app.route("/home")
def home():
    refresh_files()
    return render_template("index.html", detectedFile=detectedFile)

@app.route("/services")
def services():
    refresh_files()
    return render_template("services.html", detectedFile=detectedFile)
@app.route("/about")
def about():
    refresh_files()
    return render_template("about.html", detectedFile=detectedFile)

@app.route("/login", methods=["GET", "POST"])
def login():
    global detectedFile, path
    refresh_files()
    if request.method == "POST":
        usr = request.form['username']
        pwd = request.form['password']
        key = resolveUserPwdToKey(usr, pwd)
        file_logged = ""
        for file in detectedFile:
            stripped_file = file.strip(".sm")
            if decrypt_str(key, stripped_file) == usr:
                file_logged = stripped_file
                break
        if decrypt_str(key, file_logged) == usr:
            session["username"] = usr
            file_logged += ".sm"
            session["file_logged"] = os.path.join(path, file_logged)
            session["key"] = key
            return redirect(url_for('manage_results'))
        else:
            flash("Uncorrect username or password.\n Or you don't have an account, so create one.", "error")
            return redirect(url_for('login'))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    global path, detectedFile
    refresh_files()
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        mail = request.form["mail"]
        usr = request.form['username']
        pwd = request.form['password']
        if usr == pwd:
            flash("Username and password cannot be the same.", "error")
            return render_template('register.html', username=usr)
        key = resolveUserPwdToKey(usr, pwd)
        file_name = f"{encrypt_str(key, usr)}.sm"
        if file_name in detectedFile:
            flash("An account has already been created with this user and password, please change them or you've already have an account.", "error")
            return redirect(url_for('register'))
        with open(os.path.join(path, file_name), 'w', encoding="utf-8") as file:
            data = [
                f"version: {getVersion()}",
                f"name: {name}",
                f"surname: {surname}",
                f"mail: {mail}",
                f"username: {usr}"
            ]
            
            for line in data:
                line_crypted = encrypt_str(key, line)
                file.write(line_crypted + "\n")
        refresh_files()
        flash("Account created !\nplease log in now.", "info")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

@app.route("/manage_results", methods=["POST", "GET"])
def manage_results():
    global results_sheet
    session["previous_url"] = request.url
    if request.method == "POST":
        return redirect(url_for("add_score"))
    else:
        if 'file_logged' not in session:
            flash("We don't finding your file please reconnect.", "error")
            return redirect(url_for('login'))
        elif not isinstance(results_sheet, Results) or len(results_sheet.notes) == 0:
            key = session["key"]
            file = session["file_logged"]
            if not file.endswith(".sm"):
                file += ".sm"
            session["file_logged"] = file
            results_sheet = Results(file, getVersion())
            lines = readAndDecrypteFile(key, file)
            results_sheet.parse_lines(lines)
        name = results_sheet.get_info("name")
        average = results_sheet.calcul_average
        return render_template('manage_results.html', name=name, results_sheet=results_sheet, average=average)

@app.route('/add_score', methods=["POST", "GET"])
def add_score(branch=None):
    global results_sheet
    if "previous_url" not in session:
        return redirect(url_for("login"))
    
    origin = session["previous_url"]
    
    if not branch:
        branch = request.args.get('branch', None)
    
    if request.method == "POST":
        branch = request.form['branch'].strip()
        score = request.form['score']
        name = request.form['name'].strip()
        subset = request.form.get('subset', '')
        try:
            score = float(score)
            if results_sheet:
                results_sheet.add_note(branch, score, name, subset)
                key = session["key"]
                file = session["file_logged"]
                lines = results_sheet.reconstruct_lines()
                encrypteAndWriteFile(key, lines, file)

        except ValueError:
            flash("Invalid score value", "error")
            return render_template("add_score.html", branch=branch)
        
        return redirect(origin)

    else:
        return render_template("add_score.html", branch=branch)

@app.route('/view_notes/<branch>', methods=["GET", "POST"])
def view_notes(branch):
    global results_sheet
    session["previous_url"] = request.url
    notes = [note for note in results_sheet.notes if note.branch == branch]
    key = session["key"]
    file = session["file_logged"]
    lines = results_sheet.reconstruct_lines()
    encrypteAndWriteFile(key, lines, file)
    return render_template('view_notes.html', branch=branch, results_sheet=results_sheet, notes=notes)

@app.route('/update_note/<branch>/<name>', methods=["POST"])
def update_note(branch, name):
    global results_sheet
    new_name = request.form["name"]
    score = float(request.form["score"])
    subset = request.form["subset"]
    results_sheet.update_note(branch, name, new_name, score, subset)
    return redirect(url_for('view_notes', branch=branch))

def getVersion():
    return "1.1"

if __name__ == '__main__':
    app.run(debug=True)