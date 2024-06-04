import psycopg2
from app.utils import get_all_constellations, get_all_stars, save_star_symbols, load_star_symbols
from app.menu import display_menu, show_all_stars, change_star_symbols, get_star_details

def main():
    conn = psycopg2.connect(
        host="178.154.231.252",
        port="5432",
        database="db_user10",
        user="user10",
        password="password10"
    )
    cursor = conn.cursor()

    star_symbols = load_star_symbols()

    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == '1':
            show_all_stars(cursor, star_symbols)
        elif choice == '2':
            star_symbols = change_star_symbols()
        elif choice == '3':
            get_star_details(cursor)
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из меню.")

    conn.close()


if __name__ == "__main__":
    main()