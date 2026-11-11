# Python Network Scanner 🌐

A simple Python-based network scanner designed to discover active devices within an authorized local IPv4 network using ICMP ping requests.

This project helps users understand basic network discovery and learn how to identify active devices in a local area network (LAN).

## 🚀 Features

- **Network Scanning** – Discovers devices within a specified private IPv4 network.
- **IP Address Detection** – Identifies IP addresses of devices responding to ping requests.
- **Device Status** – Displays whether a device is online.
- **Network Validation** – Validates the provided network address.
- **Cross-Platform Support** – Supports Windows and Linux ping commands.
- **Scan Summary** – Displays the total number of responding devices.

## 🛠️ Technologies Used

- Python 3
- ipaddress
- subprocess
- platform

## 📋 Requirements

- Python 3.10 or later.
- Windows or Linux operating system.
- Connection to an authorized local network.

## 📥 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/pradipta-web/python-network-scanner.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-network-scanner
   ```

3. Run the application:

   **Windows:**
   ```bash
   py main.py
   ```

   **Linux:**
   ```bash
   python3 main.py
   ```

## 💻 Usage

1. Run the Python application.
2. Enter your private IPv4 network address in CIDR notation.
3. Wait for the scanning process to complete.
4. View the discovered active IP addresses.

### Example Input

```text
192.168.1.0/24
```

### Example Output

```text
Starting Network Scanner...
Target Network: 192.168.1.0/24
---------------------------------------------

[ONLINE] 192.168.1.1
[ONLINE] 192.168.1.5
[ONLINE] 192.168.1.10

---------------------------------------------
Scan completed!
Active Devices: 3
```

*Note: The output above is an example. Devices that block ICMP ping requests may not be detected.*

## 📚 Learning Objectives

This project was created to improve practical knowledge of:

- Python programming.
- Computer networking.
- IPv4 addressing and CIDR notation.
- ICMP ping requests.
- Local network discovery.
- Network troubleshooting.

## ⚠️ Disclaimer

This tool is intended for educational purposes and authorized network administration only.

Only scan networks that you own or have explicit permission to examine.

## 👨‍💻 Author

**Pradipta Raditya**

GitHub: [@pradipta-web](https://github.com/pradipta-web)

---

*Built for learning Python programming and computer networking.*