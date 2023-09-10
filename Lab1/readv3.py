import sys
from scapy.all import *

def extract_icmp_payloads(packet):
    payloads = []
    if packet.haslayer(ICMP) and packet[ICMP].type == 8:
        if Raw in packet:
            payloads.append(packet[Raw].load)
    return payloads

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py input.pcapng")
        sys.exit(1)

    input_file = sys.argv[1]

    packets = rdpcap(input_file)
    cipher_text = ""

    for packet in packets:
        payloads = extract_icmp_payloads(packet)
        for payload in payloads:
            first_char = payload[0:1].decode('utf-8', errors='ignore')
            cipher_text += first_char

    for shift in range(26):
        decrypted_text = caesar_decrypt(cipher_text, shift)
        if "tog" in decrypted_text:
            print(f"\033[92m {shift}: {decrypted_text}\033[0m")
        else:
            print(f" {shift}: {decrypted_text}")

if __name__ == "__main__":
    main()
