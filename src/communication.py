import random


class CommunicationLink:
    def __init__(self, packet_loss_rate=0.2):
        self.packet_loss_rate = packet_loss_rate

    def transmit(self, packet):
        if random.random() < self.packet_loss_rate:
            return None

        return packet