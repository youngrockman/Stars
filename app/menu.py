import textwrap
from app.utils import get_all_constellations, get_all_stars, save_star_symbols, display_star_map

def display_menu():
    print("\nМеню:")
    print("1. Показать карту звездного неба")
    print("2. Изменить символы отображения звезд")
    print("3. Получить подробную информацию о звезде")
    print("4. Выйти")

def show_star_map(cursor, star_symbols):
    stars = get_all_stars(cursor)
    display_star_map(stars, star_symbols)

def change_star_symbols():
    new_symbols = {}
    for size in ["большая", "средняя", "маленькая"]:
        new_symbols[size] = input(f"Введите символ для {size} звезды: ")
    save_star_symbols(new_symbols)
    print("Символы успешно обновлены.")
    return new_symbols

def get_star_details(cursor):
    stars = get_all_stars(cursor)
    constellations = get_all_constellations(cursor)

    user_input = input("Введите порядковый номер или название звезды: ")
    selected_star = None

    if user_input.isdigit():
        star_index = int(user_input)
        if 1 <= star_index <= len(stars):
            selected_star = stars[star_index - 1]
    else:
        selected_star = next((star for star in stars if star.name.lower() == user_input.lower()), None)

    if selected_star:
        const_name = next(c.name for c in constellations if c.id == selected_star.constellation_id)
        const_desc = next(c.description for c in constellations if c.id == selected_star.constellation_id)
        print(f"\nНазвание звезды: {selected_star.name}")
        print(f"Полное описание: {textwrap.fill(selected_star.description, width=80)}")
        print(f"Координаты: ({selected_star.x}, {selected_star.y})")
        print(f"Созвездие: {const_name}")
        print(f"Описание созвездия: {textwrap.fill(const_desc, width=80)}")
    else:
        print("Звезда не найдена.")
