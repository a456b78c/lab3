import pyfiglet

def generate_ascii_art(text, font="standard", symbol=None, width=80):
    if symbol:
        art = pyfiglet.figlet_format(text, font=font, width=width).replace('#', symbol)
    else:
        art = pyfiglet.figlet_format(text, font=font, width=width)
    return art
