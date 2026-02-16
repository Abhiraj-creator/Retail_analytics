import sqlite3

def revenue():
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COALESCE(SUM(p.price * oi.quantity), 0)
    FROM orderItems oi
    JOIN products p ON oi.product_id = p.product_id
    """)

    result = cursor.fetchone()[0]
    conn.close()
    return result
