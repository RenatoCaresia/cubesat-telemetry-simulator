import time
from telemetry import CubeSat


satellite = CubeSat()

print("CubeSat Telemetry Simulator")
print("---------------------------")

while True:
    satellite.update_state()

    telemetry_data = satellite.generate_telemetry()

    print(telemetry_data)

    time.sleep(2)