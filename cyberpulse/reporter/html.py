from datetime import datetime
from typing import List, Dict

class HTMLReporter:
    def generate(self, data: List[Dict], filename: str):
        html = f"""
        <!DOCTYPE html>
        <html>
        <head><title>CyberPulse Report</title>
        <style>
            body {{ font-family: monospace; background: #0a0a0a; color: #00ff00; padding: 20px; }}
            h1 {{ color: #00ff00; text-align: center; }}
            table {{ width: 100%; border-collapse: collapse; }}
            th, td {{ border: 1px solid #00ff00; padding: 10px; }}
            th {{ background: #1a1a1a; }}
        </style>
        </head>
        <body>
            <h1>🌐 CyberPulse Report</h1>
            <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <h2>Devices</h2>
            <table>
                <tr><th>IP</th><th>MAC</th><th>Vendor</th></tr>
        """
        for device in data:
            html += f"<tr><td>{device.get('ip','')}</td><td>{device.get('mac','')}</td><td>{device.get('vendor','')}</td></tr>"
        html += """
            </table>
            <p style="margin-top:20px;">🔒 CyberPulse v2.0</p>
        </body>
        </html>
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
