import time
from telemetry import CubeSat


satellite = CubeSat()

print("CubeSat Telemetry Simulator")
print("---------------------------")

while True:
    satellite.update_state()

    alerts = satellite.check_alerts()

    telemetry_data = satellite.generate_telemetry()

    print(telemetry_data)

    for alert in alerts:
        print(alert)

    time.sleep(2)