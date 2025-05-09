import sqlite3

def create_table():
    conn = sqlite3.connect('tweets.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tweets
                 (id TEXT PRIMARY KEY, created_at TEXT, text TEXT, user TEXT)''')
    conn.commit()
    conn.close()

def insert_tweet(tweet):
    conn = sqlite3.connect('tweets.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO tweets (id, created_at, text, user) VALUES (?, ?, ?, ?)",
              (tweet.id_str, tweet.created_at, tweet.text, tweet.user.screen_name))
    conn.commit()
    conn.close()
