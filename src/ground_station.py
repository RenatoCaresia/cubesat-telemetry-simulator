class GroundStation:
    def __init__(self, name):
        self.name = name
        self.received_packets = 0
        self.last_sequence = 0

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

