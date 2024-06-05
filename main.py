import psycopg2
from app.utils import load_star_symbols
from app.menu import display_menu, show_star_map, change_star_symbols, get_star_details

def main():
    conn = psycopg2.connect(
        host="195.80.51.6",
        port="5432",
        database="postgres",
        user="postgres",
        password="123"
    )
    cursor = conn.cursor()

    star_symbols = load_star_symbols()

    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == '1':
            show_star_map(cursor, star_symbols)
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
