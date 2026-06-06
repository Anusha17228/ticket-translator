import sqlite3

def init_db():
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            language TEXT,
            original_text TEXT,
            english_text TEXT,
            reply_english TEXT,
            reply_translated TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ Database ready!")

def save_to_db(filename, language, original, english, reply_en, reply_tr):
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tickets 
        (filename, language, original_text, english_text, 
         reply_english, reply_translated)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (filename, language, original, english, reply_en, reply_tr))
    conn.commit()
    conn.close()
