from termcolor import colored

def colorize_text(text, color):
    available_colors = ['red', 'green', 'blue', 'yellow', 'magenta']
    if color not in available_colors:
        raise ValueError(f"Колір '{color}' не підтримується. Доступні кольори: {', '.join(available_colors)}")
    
    return colored(text, color)
