import random
from datetime import datetime


def generate_telemetry():

    telemetry = {

        "timestamp": datetime.now().isoformat(),
        "temperature_c": round(random.uniform(10,40), 2),
        "battery_percent": round(random.uniform(60,100), 2),
        "altitude_km": round(random.uniform(490,520), 2),
        "velocity_km_s": round(random.uniform(7.5,7.8), 2),
        "signal_dbm": round(random.uniform(-90,-60), 2),
    }

    return telemetry

