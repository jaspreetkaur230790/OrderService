import sqlite3

conn = sqlite3.connect('payments.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS payments (
    id TEXT PRIMARY KEY,
    item_name TEXT NOT NULL,
    amount INTEGER NOT NULL,
    status TEXT NOT NULL
)
''')
conn.commit()
conn.close()