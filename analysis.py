import sqlite3

def run_queries(sqlite_path='user_history.db'):
    conn = sqlite3.connect(sqlite_path)
    cursor = conn.cursor()

    print("1. Unique email addresses:")
    for row in cursor.execute("SELECT DISTINCT email FROM user_history"):
        print(row)

    print("\n2. Count of emails per day:")
    for row in cursor.execute("SELECT DATE(date), COUNT(*) FROM user_history GROUP BY DATE(date)"):
        print(row)

    print("\n3. First and Last email per email address:")
    for row in cursor.execute("""
        SELECT email, MIN(date) as first_date, MAX(date) as last_date
        FROM user_history
        GROUP BY email
    """):
        print(row)

    print("\n4. Total emails by domain:")
    for row in cursor.execute("""
        SELECT SUBSTR(email, INSTR(email, '@') + 1) AS domain, COUNT(*) 
        FROM user_history
        GROUP BY domain
    """):
        print(row)

    conn.close()
