def save_to_file(art, filename="ascii_art.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(art)
    print(f"ASCII-арт збережено у {filename}")
