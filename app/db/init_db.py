import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'retail_ai.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create tables if not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            store_id INTEGER,
            demand_prediction TEXT,
            inventory_status TEXT,
            customer_info TEXT,
            price_recommendation TEXT,
            llm_summary TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            agent TEXT,
            action TEXT,
            result TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()
    print("[DB INIT] SQLite database initialized at:", DB_PATH)

if __name__ == "__main__":
    init_db()
