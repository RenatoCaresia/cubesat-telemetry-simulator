import random
from datetime import datetime

class CubeSat:
    def __init__(self):
        self.battery_percent = 100.0
        self.temperature_c = 25.0
        self.altitude_km = 500.0
        self.velocity_km_s = 7.6
        self.signal_dbm = -70.0

    def update_state(self):
        self.battery_percent -= 0.2

        self.temperature_c += random.uniform(-0.5, 0.5)
        self.altitude_km += random.uniform(-0.2, 0.2)
        self.velocity_km_s += random.uniform(-0.01, 0.01)
        self.signal_dbm += random.uniform(-1, 1)

    def generate_telemetry(self):
        return {
            "timestamp": datetime.now().isoformat(),
            "temperature_c": round(self.temperature_c, 2),
            "battery_percent": round(self.battery_percent, 2),
            "altitude_km": round(self.altitude_km, 2),
            "velocity_km_s": round(self.velocity_km_s, 2),
            "signal_dbm": round(self.signal_dbm, 2)
        }

