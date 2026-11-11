import subprocess
import ipaddress
import platform

def scan_network(network):

    try:
        net = ipaddress.ip_network(network, strict=False)

        # Only allow private IPv4 networks up to /24
        if not isinstance(net, ipaddress.IPv4Network):
            print("[ERROR] Only IPv4 networks are supported.")
            return

        if not net.is_private or net.num_addresses > 256:
            print("[ERROR] Enter a private network with /24 or smaller scope.")
            return

        print("\nStarting Network Scanner...")
        print(f"Target Network: {net}")
        print("-" * 45)

        active_devices = []

        for ip in net.hosts():

            command = ["ping"]

            if platform.system().lower() == "windows":
                command += ["-n", "1", "-w", "500"]
            else:
                command += ["-c", "1", "-W", "1"]

            command.append(str(ip))

            result = subprocess.run(
                command,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=3
            )

            if result.returncode == 0:
                active_devices.append(str(ip))
                print(f"[ONLINE] {ip}")

        print("-" * 45)
        print(f"Scan completed!")
        print(f"Active Devices: {len(active_devices)}")

    except ValueError:
        print("[ERROR] Invalid network format!")

    except subprocess.TimeoutExpired:
        print("[TIMEOUT] Request timed out.")

network = input("Enter your local network (example: 192.168.1.0/24): ")

scan_network(network)