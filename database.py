import sqlite3
import hashlib

conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    phone TEXT PRIMARY KEY,
    password TEXT
)
""")
conn.commit()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(name, phone, password):
    if len(phone) != 10 or not phone.isdigit():
        return "Invalid phone"

    try:
        c.execute("INSERT INTO users VALUES (?, ?, ?)",
                  (name, phone, hash_password(password)))
        conn.commit()
        return "Success"
    except:
        return "Exists"

def login_user(phone, password):
    c.execute("SELECT * FROM users WHERE phone=? AND password=?",
              (phone, hash_password(password)))
    return c.fetchone()
