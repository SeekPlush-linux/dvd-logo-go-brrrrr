import os
from time import sleep
import random
import argparse

parser = argparse.ArgumentParser(description='A Simple DVD Logo Screensaver, made by Seek Plush (https://github.com/SeekPlush-linux).')
parser.add_argument('--text', type=str, default=None,
                   help='Custom text to display (use \\n for newlines)')
parser.add_argument('--delay', type=float, default=0.1,
                   help='Animation refresh rate (default: 0.1)')
parser.add_argument('--dx-min', type=int, default=1,
                   help='Minimum X movement speed (default: 1)')
parser.add_argument('--dx-max', type=int, default=3,
                   help='Maximum X movement speed (default: 3)')
parser.add_argument('--dy-min', type=int, default=1,
                   help='Minimum Y movement speed (default: 1)')
parser.add_argument('--dy-max', type=int, default=2,
                   help='Maximum Y movement speed (default: 2)')
parser.add_argument('--debug', action='store_true',
                   help='Enable debug information')

args = parser.parse_args()

text = args.text.replace("\\n", "\n") if args.text is not None else """   ████████████████████       █████████████████
   █████████████████████    █████████████████████
   ██████    ███████████   ████████████    ██████
  ██████     ██████████████████ ██████     ██████
  ██████   ███████  ██████████  ██████   ███████
 ████████████████    ███████   ████████████████
 ████████████         █████    ████████████
                      ███
       █████████████████████████████████
███████████████████         ██████████████████
██████████████████         ███████████████████
      █████████████████████████████████"""
delay = args.delay
dx_min = args.dx_min
dx_max = args.dx_max
dy_min = args.dy_min
dy_max = args.dy_max
debug = args.debug

size = os.get_terminal_size()
width = size.columns
height = size.lines
x = 0
y = 0
dx = random.randint(dx_min, dx_max)
dy = random.randint(dy_min, dy_max)
text_lines = text.count("\n") + 1
text_max_length = len(max(text.split("\n"), key=len))
color = random.randint(30, 37)

while True:
    os.system("clear")

    if debug:
        print("\u001b[37m\n  Debug Info:\n"
              f"  Width: {width}\n"
              f"  Height: {height}\n"
              f"  Pos: {x},{y}\n"
              f"  Delta Pos: {dx},{dy}\n"
              f"  Text Lines: {text_lines}\n"
              f"  Text Max Length: {text_max_length}\n"
              f"  Current ANSI color: {color}\u001b[0m", end="", flush=True)
    print("\u001b[1000A\u001b[1000D", end="", flush=True)

    if x + text_max_length >= width or x <= 0:
        color = random.randint(30, 37)
        dx = random.randint(dx_min, dx_max) if dx > 0 else -(random.randint(dx_min, dx_max))
        dy = random.randint(dy_min, dy_max) if dy > 0 else -(random.randint(dy_min, dy_max))
        dx *= -1
        x = max(0, min(width - text_max_length, x))

    if y + text_lines >= height or y <= 0:
        color = random.randint(30, 37)
        dx = random.randint(dx_min, dx_max) if dx > 0 else -(random.randint(dx_min, dx_max))
        dy = random.randint(dy_min, dy_max) if dy > 0 else -(random.randint(dy_min, dy_max))
        dy *= -1
        y = max(0, min(height - text_lines, y))

    if y > 0:
        print(f"\u001b[{y}B", end="", flush=True)

    if x > 0:
        splitted_text = text.split("\n")
        print(f"\u001b[{color};1m{"".join([f"\u001b[{x}C{splitted_text[i]}\n" for i in range(text.count("\n"))])}\u001b[{x}C{splitted_text[text.count("\n")]}\u001b[0m", end="", flush=True)
    else:
        print(f"\u001b[{color};1m{text}\u001b[0m", end="", flush=True)

    print("\u001b[1000A\u001b[1000D", end="", flush=True)

    x += dx
    y += dy

    sleep(delay)
