import time
from telemetry import CubeSat
from ground_station import GroundStation
from communication import CommunicationLink

satellite = CubeSat()
ground_station = GroundStation("Santos Ground Station")
communication_link = CommunicationLink()

print("CubeSat Telemetry Simulator")
print("---------------------------")

while True:
    satellite.update_state()

    alerts = satellite.check_alerts()

    telemetry_data = satellite.generate_telemetry()

    received_packet = communication_link.transmit(telemetry_data)

    if received_packet is not None:
        ground_station.receive_telemetry(received_packet)

    else:
        print(
        f"\nPacket #{telemetry_data['sequence']} LOST"
    )

    for alert in alerts:
        print(alert)

    time.sleep(2)