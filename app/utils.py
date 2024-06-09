import json
from app.classes import Constellation, Star
import shutil
import random
import string

def load_star_symbols():
    try:
        with open('star_symbols.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"большая": "*", "средняя": "+", "маленькая": "."}

def save_star_symbols(symbols):
    with open('star_symbols.json', 'w', encoding='utf-8') as file:
        json.dump(symbols, file, ensure_ascii=False)

def get_all_constellations(cursor):
    cursor.execute("SELECT id, name, description FROM constellations")
    return [Constellation(*row) for row in cursor.fetchall()]

def get_all_stars(cursor):
    cursor.execute("SELECT id, name, x_coordinate, y_coordinate, description, constellation_id, size FROM stars")
    return [Star(*row) for row in cursor.fetchall()]

def display_star_map(stars, star_symbols):
    # Определяем размеры консоли
    console_size = shutil.get_terminal_size((80, 20))
    console_width, console_height = console_size.columns - 2, console_size.lines - 4

    # Определяем размеры карты на основе координат звезд
    min_x, max_x = min(star.x for star in stars), max(star.x for star in stars)
    min_y, max_y = min(star.y for star in stars), max(star.y for star in stars)
    star_map_width = max_x - min_x
    star_map_height = max_y - min_y

    # Рассчитываем масштаб, чтобы звезды уместились на карте
    scale_x = console_width / star_map_width if star_map_width > 0 else 1
    scale_y = console_height / star_map_height if star_map_height > 0 else 1
    scale = min(scale_x, scale_y)

    # Создаем пустую карту
    sky_map = [[" " for _ in range(console_width)] for _ in range(console_height)]

    # Заполняем карту звездами и их названиями
    for star in stars:
        symbol = star_symbols.get(star.size, '*')
        x = int((star.x - min_x) * scale)
        y = int((star.y - min_y) * scale)

        star_representation = f"{symbol}-{star.name}"

        if 0 <= x < console_width and 0 <= y < console_height:
            # Проверка, не выходит ли звезда за пределы карты
            if x + len(star_representation) > console_width:
                star_representation = star_representation[:console_width - x]

            for i, char in enumerate(star_representation):
                if x + i < console_width:
                    sky_map[y][x + i] = char

    # Отображение карты
    print("\n+" + "-" * console_width + "+")
    for row in sky_map:
        aligned_row = ''.join(row)
        print("|" + aligned_row.ljust(console_width) + "|")
    print("+" + "-" * console_width + "+")