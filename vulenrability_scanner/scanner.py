import socket

# Common ports to scan
ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389]

# Ask user for target
target = input("Enter target IP or website: ")

print(f"\nScanning target: {target}\n")

for port in ports:
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port} is open")
    else:
        print(f"[CLOSED] Port {port} is closed")

    scanner.close()