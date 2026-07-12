import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Yeh code Render ke Logs mein print karega ki server ke andar exactly kya-kya rakha hai
    print("=== DEBUGGING INFO ===")
    print("Current Folder:", os.getcwd())
    print("Files in Main Folder:", os.listdir('.'))
    if os.path.exists('templates'):
        print("Files inside 'templates':", os.listdir('templates'))
    else:
        print("WARNING: 'templates' folder is MISSING in Render!")
    print("======================")
    
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
