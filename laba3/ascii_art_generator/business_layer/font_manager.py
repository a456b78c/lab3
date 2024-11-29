import pyfiglet

def list_available_fonts():
    return pyfiglet.FigletFont.getFonts()

def select_font(font_name):
    available_fonts = list_available_fonts()
    if font_name in available_fonts:
        return font_name
    else:
        raise ValueError(f"Шрифт '{font_name}' не існує. Доступні шрифти: {', '.join(available_fonts)}")
