# import sqlite3  # for database building
import sqlite3

from flask import Flask # facilitate flask webserving
from flask import render_template  # facilitate jinja templating
from flask import request  # facilitate form submission
from flask import session  # facilitate user sessions\
from flask import redirect
import os

app=Flask(__name__) # create Flask object
app.secret_key = os.urandom(32)     #randomized string for SECRET KEY (for interacting with operating system)

dirname = os.path.dirname(__file__)

DB_FILE = os.path.join(dirname, "tables.db")

#-------------------------DataBase-------------------------
db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor()  # facilitate db ops -- you will use cursor to trigger db events

# three tables: users, orders in cart, order history
c.execute(
    "CREATE TABLE IF NOT EXISTS users(email TEXT PRIMARY KEY, password TEXT)")
db.commit()  # save changes
#-------------------------DataBase-------------------------

# DO NOT EDIT ABOVE

def render_template_with_email(template):
    emailStr = session.get('email', None)
    print("email is " + str(emailStr) + " in render_template_with_email")
    return render_template(template, email=emailStr)

@app.route("/")
def index():
        return render_template_with_email("index.html")

@app.route("/battering_ram")
def battering_ram():
        return render_template_with_email("battering_ram.html")

@app.route("/cluster_bomb")
def cluster_bomb():
        return render_template_with_email("cluster_bomb.html")

@app.route("/pitchfork")
def pitchfork():
        return render_template_with_email("pitchfork.html")

@app.route("/sniper")
def sniper():
        return render_template_with_email("sniper.html")

@app.route("/profile")
def profile():
    username = session.get('email', None)
    cadmin = isadmin()
    return render_template("profile.html", email = username, admin=cadmin)

@app.route("/change_password", methods=['POST'])
def change_password():
    username = session.get('email', None)
    if username:
        cadmin = isadmin()
        input_password = request.form['passone']
        input_confirm_password = request.form['passtwo']
        if input_password != input_confirm_password:
            return render_template('profile.html', email = username, admin=cadmin, message = "Passwords do not match. Please try again.")
        if input_password == '':
            return render_template('profile.html', email = username, admin=cadmin, message = "Please enter a Password")
        else:
            c.execute("UPDATE users SET password = ? WHERE email = ?", (input_password, username))
            return render_template('profile.html', email = username, admin=cadmin, message = "Password Successfully Changed")
    else:
        return redirect("/")

@app.route("/SUPER_SECRET_PASSWORDS")
def admin():
    c.execute("select email, password FROM users")
    data = c.fetchall()
    return render_template("SUPER_SECRET_PASSWORDS.html", email=session.get('email', None), response=data)

#-------------------------ACCOUNTS-------------------------
def isadmin():
    if session.get('email', None) == 'admin@burpintrude':
        return True
    else:
        return False

def check_email(email):
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    if c.fetchone():
        return True
    else:
        return False
    
def insert_account(email, password):
    c.execute("INSERT INTO users (email, password) VALUES (?, ?)",
              (email, password))
    db.commit()

@app.route("/register", methods=['POST'])
def register():

    # POST
    if request.method == 'POST':
        input_email = request.form['email']
        input_password = request.form['password']
        confirm_password = request.form['confirm_password']

        response = {
            'error': '',
            'success': ''
        }
        # if no registration info is inputted into the fields
        if input_email.strip() == '' or input_password.strip() == '' or confirm_password.strip() == '':
            # return json response instead of rendering template
            if input_email.strip() == '':
                response['error'] = "Please enter a email."

            if input_password.strip() == '':
                response['error'] += "Please enter a password."

            if confirm_password.strip() == '':
                response['error'] += "Please confirm your password."

            if input_password.strip() != confirm_password.strip():
                response['error'] += "Passwords do not match."

            response['success'] = "false"
            # return render_template_with_email('register.html', message=response['error'])
            # return home page with url params
            return redirect(f"/?error={response['error']}&modal=register")

            # if info is entered into fields
        else:
            # Checks for existing email in accounts table
            # var = (input_email,)
            # c.execute("select email from accounts where email=?", var)\

            if check_email(input_email):
                response['error'] = "email is already taken. Please select another email. "
                response['success'] = "false"
                return redirect(f"/?error={response['error']}&modal=register")

            # if email is not taken
            else:
                # if passwords match
                if input_password == confirm_password:
                    # insert into accounts table
                    insert_account(input_email, input_password)
                    response['success'] = "true"
                    if request.method == 'GET':  # For 'get'
                        # stores email in session
                        session['email'] = request.args['email']

                    if request.method == 'POST':  # For 'post'
                        # stores email in session
                        session['email'] = request.form['email']
                        
                    return redirect(f"/?success=Successfully registered!&modal=register")
                # if passwords don't match
                else:
                    response['error'] = "Passwords do not match. "
                    response['success'] = "false"
                    print("Passwords do not match")
                    return redirect(f"/?error={response['error']}&modal=register")
    else:
        # return status code 405 (method not allowed)
        return 405

# login process

@app.route("/login", methods=['GET', 'POST'])
def login():
    # Already logged in
    if 'email' in session:
        print("user is logged in as " +
              session['email'] + " is already logged in. Redirecting to /")
        return redirect("/")

    # POST
    if request.method == 'POST':
        input_email = request.form['email']
        input_password = request.form['password']

    # Searches accounts table for user-password combination
    c.execute("select email from users where email=? and password=?;",
              (input_email, input_password))

    # login_check
    if c.fetchone():
        print("Login success!")
        if request.method == 'GET':  # For 'get'
            # stores email in session
            session['email'] = request.args['email']

        if request.method == 'POST':  # For 'post'
            # stores email in session
            session['email'] = request.form['email']

        return redirect("/")

    else:
        print("Login failed")
        error_msg = ''
        email_check = "select email from users where email=?;"
        password_check = "select email from users where password=?;"

        # email check
        c.execute(email_check, (input_email,))
        if not c.fetchone():
            error_msg += "email is incorrect or not found. "

        # Password check
        c.execute(password_check, (input_password,))
        if not c.fetchone():
            error_msg += "Password is incorrect or not found. "

        error_msg += "Please try again."
        return redirect(f"/?error={error_msg}&modal=login")

# logout and redirect to login page


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    # remove the email from the session if it's there
    session.pop('email', None)
    print("user has logged out. Redirecting to /login")
    return redirect("/")

#-------------------------ACCOUNTS-------------------------

# DO NOT EDIT BELOW
if __name__ == "__main__":
        app.run()