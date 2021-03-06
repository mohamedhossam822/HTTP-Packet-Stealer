import socket
import binascii


class IpPacket(object):
    """
    Represents the *required* data to be extracted from an IP packet.
    """

    def __init__(self, protocol, ihl, source_address, destination_address, payload):
        self.protocol = protocol
        self.ihl = ihl
        self.source_address = source_address
        self.destination_address = destination_address
        self.payload = payload


class TcpPacket(object):
    """
    Represents the *required* data to be extracted from a TCP packet.
    """

    def __init__(self, src_port, dst_port, data_offset, payload):
        self.src_port = src_port
        self.dst_port = dst_port
        # As far as I know, this field doesn't appear in Wireshark for some reason.
        self.data_offset = data_offset
        self.payload = payload


def parse_raw_ip_addr(raw_ip_addr: bytes) -> str:
    # Converts a byte-array IP address to a string
    # the input is on the form b'\xaa\xab'... a byte array
    return "0.0.0.0"


def parse_application_layer_packet(ip_packet_payload: bytes) -> TcpPacket:
    packet_hex = binascii.hexlify(packet)
    # Parses raw bytes of a TCP packet
    # That's a byte literal (~byte array) check resources section
    return TcpPacket(-1, -1, -1, b"")


def parse_network_layer_packet(ip_packet: bytes) -> IpPacket:
    packet_hex = binascii.hexlify(packet)
    # Parses raw bytes of an IPv4 packet
    # That's a byte literal (~byte array) check resources section
    return IpPacket(-1, -1, "0.0.0.0", "0.0.0.0", b"")


def main():
    # Un-comment this line if you're getting too much noisy traffic.
    # to bind to an interface on your PC. (or you can simply disconnect from the internet)

    # iface_name = "lo"
    # stealer.setsockopt(socket.SOL_SOCKET,
    #                    socket.SO_BINDTODEVICE, bytes(iface_name, "ASCII"))

    stealer = socket.socket(socket.AF_INET, socket.SOCK_RAW, 0x0011)

    while True:
        packet, addr = stealer.recvfrom(4096)

        # 22,23 characters must be 6 for tcp

        print(type(packet_hex))
        print(packet_hex)

        parse_raw_ip_addr(addr)

        IPtObj = parse_network_layer_packet(packet)  # IP Packet obj
        # Print IP obj
        TCPObj = parse_application_layer_packet(ipPacketObj.ip_packet_payload)
        # Print TCP Obj if exists


if __name__ == "__main__":
    main()
