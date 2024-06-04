import json
from app.classes import Constellation, Star

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

def display_stars(stars, constellations, star_symbols):
    constellation_map = {c.id: c.name for c in constellations}

    stars_by_constellation = {}
    for star in stars:
        if star.constellation_id not in stars_by_constellation:
            stars_by_constellation[star.constellation_id] = []
        stars_by_constellation[star.constellation_id].append(star)

    # Отображение звезд в рамке
    print("\n+" + "-"*78 + "+")
    for const_id, stars_list in stars_by_constellation.items():
        const_name = constellation_map[const_id]
        print(f"|{const_name.center(78)}|")
        for star in stars_list:
            symbol = star_symbols.get(star.size, '*')
            star_info = f" {symbol} {star.name:<20} ({star.x:.4f}, {star.y:.4f}) "
            padding = 78 - len(star_info) - 2
            print(f"| {star_info}{' ' * padding}|")
    print("+" + "-"*78 + "+")

    # Отображение подробной информации о звездах
    for i, star in enumerate(stars, start=1):
        const_name = constellation_map[star.constellation_id]
        desc = star.description if len(star.description) <= 60 else star.description[:57] + "..."
        print(f"{i:2}. {star.name:<20} {const_name:<15} {desc}")

