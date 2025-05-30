from flask import Flask, render_template,request, redirect, flash, url_for
import string
import random
from urllib.parse import urlparse
import sqlite3
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'secret'  # Needed for flash messages

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def init_db():
    conn = sqlite3.connect('url.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE NOT NULL,
            long_url TEXT NOT NULL, click_count INTEGER NOT NULL DEFAULT 0, created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
        
    if request.method == 'POST':
        long_url = request.form['long_url']
        
        if not url_validator(long_url):
            flash("Invalid URL. Please include http:// or https://", "error")
            return redirect(url_for('index'))
        
        short_code = generate_short_code()
        created_at =datetime.now()

        # Save into DB
        conn = sqlite3.connect('url.db')
        c = conn.cursor()
        c.execute("INSERT INTO urls (short_code, long_url, click_count, created_at) VALUES (?, ?, ?, ?)",(short_code, long_url, 0, created_at))

        conn.commit()
        conn.close()
        
        short_url = request.host_url + short_code  # this is the full short URL

        flash("Success! URL has been shortened.", "success")

    return render_template('index.html', short_url=short_url)

import sqlite3



@app.route('/<short_code>')
def redirect_short_url(short_code):
    conn = sqlite3.connect('url.db')
    c = conn.cursor()

    # Fetch the long URL
    c.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,))
    result = c.fetchone()

    if result:
        long_url = result[0]

        # Update click count BEFORE closing the connection
        c.execute("UPDATE urls SET click_count = click_count + 1 WHERE short_code = ?", (short_code,))
        conn.commit()
        conn.close()

        return redirect(long_url)  # Now safely redirect
    else:
        conn.close()
        return "Short URL not found", 404

@app.route('/analytics')
def analytics():
    conn = sqlite3.connect('url.db')
    c = conn.cursor()
    c.execute("SELECT short_code, long_url, click_count, created_at FROM urls")
    urls = c.fetchall()
    conn.close()
    return render_template('analytics.html', urls=urls)

def show_all_urls():
    conn = sqlite3.connect('url.db')
    c = conn.cursor()
    c.execute("SELECT * FROM urls")
    print(c.fetchall())
    conn.close()

show_all_urls()  # Call this in your index() function or when app starts


def url_validator(long_url):
    try:
        result = urlparse(long_url)
        return all([result.scheme, result.netloc])
    except:
        return False
    
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
