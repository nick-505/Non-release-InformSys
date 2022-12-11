from app import db, app
from app.db_connection import connect

def get_employee():
    conn = connect()
    with conn.cursor() as cur:
        sql = f'SELECT id, name, subject, phone, email FROM employees'
        cur.execute(sql)
        return cur.fetchall()