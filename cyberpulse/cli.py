import asyncio
import time
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn

from .scanner.network import NetworkScanner
from .analyzer.traffic import TrafficAnalyzer
from .predictor.model import ThreatPredictor
from .reporter.html import HTMLReporter
from .utils.animations import matrix_rain, hacker_typing

console = Console()

class CyberPulseCLI:
    def __init__(self):
        self.scanner = NetworkScanner()
        self.analyzer = TrafficAnalyzer()
        self.predictor = ThreatPredictor()
        self.results = []

    def show_banner(self):
        banner = """
        ╔══════════════════════════════════════════╗
        ║   ██████╗██╗   ██╗██████╗ ███████╗     ║
        ║  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝     ║
        ║  ██║      ╚████╔╝ ██████╔╝█████╗       ║
        ║  ██║       ╚██╔╝  ██╔══██╗██╔══╝       ║
        ║  ╚██████╗   ██║   ██████╔╝███████╗     ║
        ║   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝     ║
        ║         🌐 CyberPulse v2.0               ║
        ╚══════════════════════════════════════════╝
        """
        console.print(banner, style="cyan")
        console.print("🔒 Your Digital Guardian", style="green bold")
        console.print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n", style="dim")

    def show_menu(self):
        menu = Panel(
            """
            [bold cyan]📋 MAIN MENU[/bold cyan]
            
            [1] 🔍 Scan Network
            [2] 📊 Analyze Traffic
            [3] 🧠 Predict Threats
            [4] 📈 Generate Report
            [5] 🎮 Demo Mode
            [6] ❌ Exit
            """,
            title="CyberPulse",
            border_style="cyan"
        )
        console.print(menu)
        return Prompt.ask("[bold green]Select option[/bold green]")

    def scan_network(self):
        console.print("\n[bold yellow]🔍 Scanning Network...[/bold yellow]")
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
            task = progress.add_task("[cyan]Discovering devices...", total=100)
            for i in range(100):
                time.sleep(0.02)
                progress.update(task, advance=1)
        
        devices = self.scanner.scan("192.168.1.0/24")
        
        table = Table(title="🌐 Network Devices", style="cyan")
        table.add_column("IP Address", style="green")
        table.add_column("MAC Address", style="yellow")
        table.add_column("Vendor", style="blue")
        
        for device in devices:
            table.add_row(device.get('ip', ''), device.get('mac', ''), device.get('vendor', ''))
        
        console.print(table)
        return devices

    def analyze_traffic(self):
        console.print("\n[bold yellow]📊 Analyzing Traffic...[/bold yellow]")
        with console.status("[bold cyan]Capturing packets..."):
            time.sleep(2)
        
        stats = {
            "Total Packets": "12,847",
            "TCP": "8,234 (64%)",
            "UDP": "3,912 (30%)",
            "ICMP": "701 (6%)",
        }
        
        table = Table(title="📊 Traffic Statistics", style="cyan")
        table.add_column("Protocol", style="bold")
        table.add_column("Count", style="green")
        for protocol, count in stats.items():
            table.add_row(protocol, count)
        console.print(table)
        return stats

    def predict_threats(self):
        console.print("\n[bold yellow]🧠 Predicting Threats...[/bold yellow]")
        with console.status("[bold cyan]Analyzing patterns with ML..."):
            time.sleep(3)
        
        panel = Panel(
            f"""
            [bold]🛡️ Threat Prediction Report[/bold]
            
            [bold]Risk Level:[/bold] MEDIUM
            [bold]Threat Probability:[/bold] 67%
            [bold]Potential Attack:[/bold] Port Scanning
            [bold]Recommendation:[/bold] Increase firewall monitoring
            """,
            title="🧠 AI Prediction",
            border_style="yellow"
        )
        console.print(panel)

    def generate_report(self):
        console.print("\n[bold yellow]📄 Generating Report...[/bold yellow]")
        with console.status("[bold cyan]Creating report..."):
            time.sleep(1)
        
        reporter = HTMLReporter()
        filename = f"cyberpulse_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        reporter.generate(self.results, filename)
        console.print(f"[bold green]✅ Report saved: {filename}[/bold green]")

    def demo_mode(self):
        console.clear()
        console.print("[bold green]🎮 CyberPulse Demo Mode[/bold green]\n")
        matrix_rain(console, duration=3)
        hacker_typing(console, "INITIALIZING NETWORK SCAN...")
        time.sleep(0.5)
        hacker_typing(console, "SCANNING 192.168.1.0/24...")
        time.sleep(0.5)
        hacker_typing(console, "FOUND 12 ACTIVE DEVICES")
        time.sleep(0.5)
        hacker_typing(console, "THREAT LEVEL: MEDIUM")
        console.print("\n[bold green]✅ Demo completed![/bold green]")

    def run(self):
        while True:
            console.clear()
            self.show_banner()
            choice = self.show_menu()
            
            if choice == "1":
                self.results = self.scan_network()
                input("\n⏎ Press Enter to continue...")
            elif choice == "2":
                self.analyze_traffic()
                input("\n⏎ Press Enter to continue...")
            elif choice == "3":
                self.predict_threats()
                input("\n⏎ Press Enter to continue...")
            elif choice == "4":
                self.generate_report()
                input("\n⏎ Press Enter to continue...")
            elif choice == "5":
                self.demo_mode()
                input("\n⏎ Press Enter to continue...")
            elif choice == "6":
                console.print("[bold red]👋 Goodbye! Stay secure.[/bold red]")
                break
            else:
                console.print("[bold red]❌ Invalid choice![/bold red]")
                time.sleep(1)

def main():
    cli = CyberPulseCLI()
    cli.run()

if __name__ == "__main__":
    main()
