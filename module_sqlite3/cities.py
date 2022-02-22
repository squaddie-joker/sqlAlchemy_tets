import sqlite3


def get_cities_from_file(f_path : str) -> set():
    with open(f_path, encoding='UTF-16') as file:
        first_line = file.readline()
        city_set = set()
        while True:
            line = file.readline()
            if (not line):
                break
            if len(line) < 3:
                continue
            city, region = line.strip().split(';')
            city_set.add((city, region))
    return city_set


def create_connection(db_path : str) -> sqlite3.Connection:
    connection = None

    try:
        connection = sqlite3.connect(db_path)
        print("Successfully connection!")
    except sqlite3.Error as err:
        print(f"Error! {err}")

    return connection 


DB_PATH = r'module_sqlite3\my_db.db'
connection = create_connection(DB_PATH)


'''
F_CITIES_PATH = r'spisok.csv'
city_set = get_cities_from_file(F_CITIES_PATH)

for item in city_set:
    print(item)
'''
