import sqlite3


connection = sqlite3.connect("data/telemetry.db")

cursor = connection.cursor()

cursor.execute("""
    SELECT
        mission_id,
        sequence,
        temperature_c,
        battery_percent,
        signal_dbm
    FROM telemetry
    ORDER BY id DESC
    LIMIT 10
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()