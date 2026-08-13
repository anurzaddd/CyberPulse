import time
import random
from rich.console import Console

def matrix_rain(console: Console, duration: int = 3):
    cols = console.width or 80
    chars = "0123456789ABCDEF"
    columns = [0] * cols
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(cols):
            if random.random() < 0.3:
                columns[i] = random.choice(chars)
        line = ""
        for i in range(cols):
            char = columns[i]
            line += f"[green]{char}[/green]" if char != 0 else " "
        console.print(line, end="")
        time.sleep(0.05)

def hacker_typing(console: Console, text: str, delay: float = 0.03):
    import sys
    for char in text:
        console.print(char, end="", style="green")
        sys.stdout.flush()
        time.sleep(delay)
    console.print()
