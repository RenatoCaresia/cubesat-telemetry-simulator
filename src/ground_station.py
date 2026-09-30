import csv
import os

class GroundStation:
    def __init__(self, name):
        self.name = name
        self.received_packets = 0
        self.last_sequence = 0
        self.log_file = "data/telemetry_log.csv"

        os.makedirs("data", exist_ok=True)
        
        if not os.path.exists(self.log_file):
            with open(self.log_file, mode="w", newline="") as file:
                writer = csv.writer(file)

                writer.writerow([
                "timestamp",
                "satellite_id",
                "sequence",
                "temperature_c",
                "battery_percent",
                "altitude_km",
                "velocity_km_s",
                "signal_dbm"
            ])

    def receive_telemetry(self, packet):
        self.received_packets += 1

        current_sequence = packet["sequence"]

        if self.last_sequence != 0 and current_sequence > self.last_sequence + 1:
            lost_packets = current_sequence - self.last_sequence - 1

            print(
            f"\nWARNING: {lost_packets} packet(s) missing "
            f"between #{self.last_sequence} and #{current_sequence}"
        )

        self.last_sequence = current_sequence

        print(f"\nGround Station: {self.name}")
        print(f"Packet #{current_sequence} received")
        print(packet)

        self.log_telemetry(packet)
        
    def log_telemetry(self, packet):
        data = packet["data"]

        with open(self.log_file, mode="a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                packet["timestamp"],
                packet["satellite_id"],
                packet["sequence"],
                data["temperature_c"],
                data["battery_percent"],
                data["altitude_km"],
                data["velocity_km_s"],
                data["signal_dbm"]
            ])
