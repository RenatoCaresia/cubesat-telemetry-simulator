import sqlite3
import os


class TelemetryDatabase:
    def __init__(self, database_path="data/telemetry.db"):
        os.makedirs("data", exist_ok=True)

        self.connection = sqlite3.connect(database_path)

        self.create_table()

    def create_table(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS telemetry (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mission_id TEXT,
                timestamp TEXT,
                satellite_id TEXT,
                sequence INTEGER,
                temperature_c REAL,
                battery_percent REAL,
                altitude_km REAL,
                velocity_km_s REAL,
                signal_dbm REAL
            )
        """)

        self.connection.commit()

    def save_packet(self, packet):
        data = packet["data"]

        cursor = self.connection.cursor()

        cursor.execute("""
            INSERT INTO telemetry (
                mission_id,
                timestamp,
                satellite_id,
                sequence,
                temperature_c,
                battery_percent,
                altitude_km,
                velocity_km_s,
                signal_dbm
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            packet["mission_id"],
            packet["timestamp"],
            packet["satellite_id"],
            packet["sequence"],
            data["temperature_c"],
            data["battery_percent"],
            data["altitude_km"],
            data["velocity_km_s"],
            data["signal_dbm"]
        ))

        self.connection.commit()