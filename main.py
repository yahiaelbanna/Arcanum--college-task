from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import bcrypt
import re

app = Flask(__name__)

# PASSWORD HASHING
def hash_password(password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password

# conn = sqlite3.connect('D:\\2025 programming\\flask project\\simplecrud.db')

#Database_setup
def init_db():
    conn = sqlite3.connect('crud.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE,
            password VARCHAR(200) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Show_all_users
def get_users():
    conn = sqlite3.connect('crud.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def get_user_with_email(email):
    conn = sqlite3.connect('crud.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users where email = ?',(email,))
    user = cursor.fetchone()
    conn.close()
    return user

# Create_account_method
def signup(data):
    conn = sqlite3.connect('crud.db', timeout=10)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (data['name'], data['email'], hash_password(data['password'])))
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    
    response = redirect(url_for('index'))
    response.set_cookie('user_id', str(user_id))
    return response

# CREATE CONTEXT FOR APP NAME
@app.context_processor
def inject_app_name():
    return dict(app_name="Arcanum")

# SIGNUP PAGE FRONT
@app.route('/signup')
def signupPage():
        return render_template('signup.html')

#SIGNUP REQUEST
@app.route('/signup', methods=['POST'])
def signupRequest():
    if request.method == 'POST':
        data = request.form
        errors = []
        
        if not data.get('name') or not data['name'].strip():
            errors.append('Name is required')
        if not data.get('email') or not data['email'].strip():
            errors.append('Email is required')
        if not data.get('password') or not data['password'].strip():
            errors.append('Password is required')

        if get_user_with_email(data['email']) is not None:
            errors.append('This email is already taken')
        
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', data['email']):
            errors.append('Invalid email format')

        if errors:
            return render_template('signup.html', errors=errors)
        
        return signup(data)
        # return redirect(url_for('index'))

@app.route('/')
def index():
    return 'hello'



if __name__ == '__main__':
    init_db()
    app.run(debug=True)