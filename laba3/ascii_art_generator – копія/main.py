from art_generator.ascii_art import generate_ascii_art
from art_generator.font_manager import select_font, list_available_fonts
from art_generator.color_manager import colorize_text
from art_generator.file_manager import save_to_file

def main():
    try:
        text = input("Введіть текст для ASCII-арту ")
        print("Доступні шрифти:", list_available_fonts())
        font = input("Оберіть шрифт: ")
        font = select_font(font)

        color = input("Оберіть колір (red', 'green', 'blue', 'yellow', 'magenta'): ")

        art = generate_ascii_art(text, font=font)
        
        colored_art = colorize_text(art, color=color)

        print(colored_art)

        save = input("Зберегти у файл? (y/n): ")
        if save.lower() == 'y':
            save_to_file(colored_art)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
