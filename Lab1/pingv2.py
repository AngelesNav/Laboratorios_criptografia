import sys
import time
from scapy.all import IP, ICMP, send

def send_icmp_packet(data, seq_num):
    packet = IP(dst='8.8.8.8') / ICMP() / data
    packet[ICMP].id = 1234  # Identificador arbitrario
    packet[ICMP].seq = seq_num
    packet[ICMP].ts_ori = int(time.time())  # Timestamp
    send(packet)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python icmp_sender.py <string>")
        sys.exit(1)

    input_string = sys.argv[1]
    seq_number = 1

    for char in input_string:
        payload = char.encode('utf-8')  # Convierte el carácter en bytes
        while len(payload) < 48:
            payload += b'\x00'  # Rellena el payload con bytes nulos si es necesario
        send_icmp_packet(payload, seq_number)
        seq_number += 1

