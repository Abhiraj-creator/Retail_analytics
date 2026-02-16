import random
import sqlite3
from datetime import datetime, timedelta


def seed_data():
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()
    for i in range(1, 51):
        cursor.execute(
            """ insert into customers (name,city,signup_date)
        values (?,?,?)""",
            (
                f"customer_{i}",
                random.choice(["Delhi", "Kalakutta", "Ramtegdi"]),
                "2026-02-30",
            ),
        )
    conn.commit()
    conn.close()
        
