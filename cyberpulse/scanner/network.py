import ipaddress
import subprocess
import platform
from typing import List, Dict, Optional

class NetworkScanner:
    def __init__(self):
        self.devices = []
        self.system = platform.system()

    def ping_host(self, ip: str) -> bool:
        param = "-n" if self.system == "Windows" else "-c"
        command = ["ping", param, "1", ip]
        try:
            result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=2)
            return result.returncode == 0
        except:
            return False

    def get_mac(self, ip: str) -> Optional[str]:
        try:
            if self.system == "Windows":
                output = subprocess.check_output(["arp", "-a", ip], text=True)
                for line in output.splitlines():
                    if ip in line and "-" in line:
                        parts = line.split()
                        for part in parts:
                            if len(part.replace("-", "")) == 12 and "-" in part:
                                return part
            else:
                output = subprocess.check_output(["arp", "-n", ip], text=True)
                for line in output.splitlines():
                    if ip in line and "ether" in line:
                        parts = line.split()
                        for i, part in enumerate(parts):
                            if part == "ether" and i + 1 < len(parts):
                                return parts[i + 1]
        except:
            pass
        return None

    def scan(self, network: str = "192.168.1.0/24") -> List[Dict]:
        self.devices = []
        try:
            net = ipaddress.ip_network(network, strict=False)
        except:
            net = ipaddress.ip_network("192.168.1.0/24")
        
        hosts = list(net.hosts())[:100]
        
        for ip_obj in hosts:
            ip = str(ip_obj)
            if self.ping_host(ip):
                mac = self.get_mac(ip)
                self.devices.append({
                    "ip": ip,
                    "mac": mac or "Unknown",
                    "vendor": self._get_vendor(mac) if mac else "Unknown"
                })
        return self.devices

    def _get_vendor(self, mac: str) -> str:
        vendors = {
            "00:11:22": "Cisco", "00:1B:24": "Siemens", "00:0A:45": "Philips",
            "00:1A:E3": "Dell", "00:23:DF": "Dell", "00:1C:23": "HP",
            "00:13:72": "IBM", "00:1A:6B": "Apple", "00:0C:29": "VMware",
            "00:50:56": "VMware", "B8:CA:3A": "Intel", "00:1B:21": "Intel",
        }
        prefix = mac[:8].upper() if mac else ""
        for key, vendor in vendors.items():
            if prefix.startswith(key):
                return vendor
        return "Unknown"
