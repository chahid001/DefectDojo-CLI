import time

symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
interval = 0.1 

RESET = '\033[0m'

BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

def display_loading_animation(text, duration=5):
    total_iterations = int(duration / interval)
    
    for _ in range(total_iterations):
        i = _ % len(symbols)
        colored_symbol = f"\033[37m{symbols[i]}{RESET}"
        print(f'\r\033[K{colored_symbol} {text}', end='')
        time.sleep(interval)

def display(text, color, duration=5):
    color_map = {
        'BOLD': BOLD,
        'DIM': DIM,
        'ITALIC': ITALIC,
        'UNDERLINE': UNDERLINE,
        'BLACK': BLACK,
        'RED': RED,
        'GREEN': GREEN,
        'YELLOW': YELLOW,
        'BLUE': BLUE,
        'MAGENTA': MAGENTA,
        'CYAN': CYAN,
        'WHITE': WHITE
    }

    colored_text = f"{color_map.get(color.upper(), '')}{text} {RESET}"
    
    display_loading_animation(text=colored_text, duration=duration)

def print_c(text, color):
    color_map = {
        'BOLD': BOLD,
        'DIM': DIM,
        'ITALIC': ITALIC,
        'UNDERLINE': UNDERLINE,
        'BLACK': BLACK,
        'RED': RED,
        'GREEN': GREEN,
        'YELLOW': YELLOW,
        'BLUE': BLUE,
        'MAGENTA': MAGENTA,
        'CYAN': CYAN,
        'WHITE': WHITE
    }
    print(f"{color_map.get(color.upper(), '')}{text}{RESET}")
