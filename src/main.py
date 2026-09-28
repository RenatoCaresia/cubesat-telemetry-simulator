import time
from telemetry import generate_telemetry


print("CubeSat Telemetry Simulator")
print("---------------------------")

while True:
    telemetry_data= generate_telemetry()

    print(telemetry_data)

    time.sleep(2)
