# database/database.py

import sqlite3
import os
from datetime import datetime

# Ensure the database directory exists
os.makedirs("database", exist_ok=True)
DB_PATH = "database/retail_ai.db"

# -------------------------------
# Initialize DB and create table
# -------------------------------
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orchestrator_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            store_id INTEGER,
            demand_forecast TEXT,
            inventory_status TEXT,
            restock_suggestion TEXT,
            customer_segment TEXT,
            price_recommendation TEXT,
            llm_summary TEXT,
            timestamp TEXT
        )
        """)
        conn.commit()


# -------------------------------
# Save orchestrator output
# -------------------------------
def save_result(
    product_id,
    store_id,
    demand_forecast,
    inventory_status,
    restock_suggestion,
    customer_segment,
    price_recommendation,
    llm_summary
):
    timestamp = datetime.utcnow().isoformat()

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO orchestrator_results (
            product_id, store_id,
            demand_forecast, inventory_status, restock_suggestion,
            customer_segment, price_recommendation, llm_summary, timestamp
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            product_id, store_id,
            demand_forecast, inventory_status, restock_suggestion,
            customer_segment, price_recommendation, llm_summary, timestamp
        ))

        conn.commit()
        print(f"[✅ DB] Saved result for Product {product_id} at Store {store_id}")


# -------------------------------
# (Optional) Fetch latest N entries
# -------------------------------
def fetch_latest_results(limit=5):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orchestrator_results ORDER BY timestamp DESC LIMIT ?", (limit,))
        return cursor.fetchall()

# Call this on startup
init_db()
