from bs4 import BeautifulSoup
import requests, folium, webbrowser, os, re



domy_opieki = [
    {"name": "Babilon", "city": "Warszawa", "pracownicy": [{"name": "Salazar Gąbka", "city": ["Gdańsk"]}, {"name": "Pior Puplik", "city": ["Łódź"]}], "pensjonariusze": [{"name": "Przemysław Laser", "city": ["Wałbrzych"]}]},
    {"name": "Puplowo", "city": "Wrocław", "pracownicy": [{"name": "Zbigniew Dzwon", "city": ["Poznań"]}, {"name": "Bartosz Pupson", "city": ["Gdańsk"]}], "pensjonariusze": [{"name": "Piotr Bizon", "city": ["Łódź"]}]},
    {"name": "Demencja i amrozja", "city": "Poznań", "pracownicy": [{"name": "Jan Czapa", "city": ["Wrocław"]}, {"name": "Jakub Pupi", "city": ["Słupsk"]}], "pensjonariusze": [{"name": "Artur Jebaka", "city": ["Suwałki"]}]}
]
def show_list(domy_opieki):
    print("Oto obecna lista domów opieki:")
    for dom_opieki in domy_opieki:
        print(f"{dom_opieki['name']}, {dom_opieki['city']}")


def add_dom_opieki(domy_opieki):
    dom_opieki_name = input("Podaj nazwę domu opieki do dodania: ")
    city_name = input("Podaj miasto, w którym znajduje sie dom opieki: ")
    domy_opieki.append({"name": dom_opieki_name, "city": city_name, "pracownicy": [], "pensjonariusze": []})
    print(f"{dom_opieki_name} zostało dodane do listy.")
    show_list(domy_opieki)


def remove_dom_opieki(domy_opieki):
    dom_opieki_name = input("Podaj nazwę domu opieki do usunięcia: ")
    city_name = input("Podaj miasto, w którym znajduje sie dom opieki: ")
    removed = False
    for dom_opieki in domy_opieki:
        if dom_opieki['name'] == dom_opieki_name and dom_opieki['city'] == city_name:
            domy_opieki.remove(dom_opieki)
            print(f"{dom_opieki_name}, {city_name} zostało usunięte z listy.")
            removed = True
            break

    if not removed:
        print(f"Nie znaleziono domu opieki {dom_opieki_name}, {city_name} na liście.")
    show_list(domy_opieki)


def update_dom_opieki(domy_opieki):
    dom_opieki_name = input("Podaj nazwę domu opieki do aktualizacji: ")
    city_name = input("Podaj miasto, w którym znajduje sie dom opieki: ")
    dom_opieki_found = False
    for dom_opieki in domy_opieki:
        if dom_opieki['name'] == dom_opieki_name and dom_opieki['city'] == city_name:
            new_name = input(f"Podaj nową nazwę dla {dom_opieki_name} w {city_name}: ")
            new_city = input(f"Podaj nowe miasto dla {new_name}: ")
            dom_opieki['name'] = new_name
            dom_opieki['city'] = new_city
            dom_opieki_found = True
            print(f"Nazwa domu opieki w {city_name} została zmieniona z {dom_opieki_name} na {new_name} w {new_city}.")
            break
    if not dom_opieki_found:
        print(f"Nie znaleziono domu opieki {dom_opieki_name} w {city_name}.")
    show_list(domy_opieki)


def show_pracownicy(domy_opieki):
    dom_opieki_name = input("Podaj nazwę domu opieki, dla którego chcesz pokazać listę zawodników: ")
    city_name = input("Podaj miasto, w którym znajduje sie dom opieki: ")
    dom_opieki_found = False
    for dom_opieki in domy_opieki:
        if dom_opieki['name'] == dom_opieki_name and dom_opieki['city'] == city_name:
            dom_opieki_found = True
            print(f"Lista pracowników dla {dom_opieki_name}, {city_name}:")
            for pracownik in dom_opieki['pracownicy']:
                print(f"{pracownik['name']}")

    if not dom_opieki_found:
        print(f"Nie znaleziono domu opieki {dom_opieki_name} w {city_name}.")


def add_pracownik(domy_opieki):
    dom_opieki_name = input("Podaj nazwę domu opieki, do którego chcesz dodać pracownika: ")
    city_name = input("Podaj miasto, w którym odbywa się to wydarzenie: ")
    dom_opieki_found = False

    for dom_opieki in domy_opieki:
        if dom_opieki['name'].lower() == dom_opieki_name.lower() and dom_opieki['city'].lower() == city_name.lower():
            pracownik_name = input(f"Podaj imię pracownika do dodania do {dom_opieki_name} w {city_name}: ")
            pracownik_city = input("Podaj miasto, z którego pochodzi pracownik: ")
            dom_opieki['pracownicy'].append({"name": pracownik_name, "city": [pracownik_city]})
            print(f"{pracownik_name} został dodany do listy zawodników wydarzenia {dom_opieki_name} w {city_name}.")
            dom_opieki_found = True
            break

    if not dom_opieki_found:
        print(f"Nie znaleziono domu opieki {dom_opieki_name} w {city_name}.")


def remove_pracownicy(domy_opieki):
    dom_opieki_name = input("Podaj nazwę domu opieki, z którego chcesz usunąć pracownika: ")
    city_name = input("Podaj miasto, w którym odbywa się to wydarzenie: ")
    dom_opieki_found = False
    for dom_opieki in domy_opieki:
        if dom_opieki['name'].lower() == dom_opieki_name.lower() and dom_opieki['city'].lower() == city_name.lower():
            pracownik_name = input(f"Podaj imię pracownika do usunięcia z {dom_opieki_name} w {city_name}: ")
            pracownicy = [pracownik['name'] for pracownik in dom_opieki['players']]
            if pracownik_name in pracownicy:
                dom_opieki['players'] = [pracownik for pracownik in dom_opieki['players'] if pracownik['name'] != pracownik_name]
                print(f"{pracownik_name} został usunięty z listy pracowników domu opieki {dom_opieki_name} w {city_name}.")
            else:
                print(f"{pracownik_name} nie znaleziono na liście pracowników domu opieki {dom_opieki_name} w {city_name}.")
            dom_opieki_found = True
            break

    if not dom_opieki_found:
        print(f"Nie znaleziono wydarzenia {dom_opieki_name} w {city_name}.")


def update_pracownicy(domy_opieki):
    dom_opieki_name = input("Podaj nazwę domu opieki, w którym chcesz zaktualizować nazwę pracownika: ").strip()
    city_name = input("Podaj miasto, w którym znajduje sie dom opieki: ").strip()
    dom_opieki_found = False

    for dom_opieki in domy_opieki:
        if dom_opieki['name'].lower() == dom_opieki_name.lower() and dom_opieki['city'].lower() == city_name.lower():
            dom_opieki_found = True
            old_pracownik_name = input(
                f"Podaj starą nazwę domu opieki do zaktualizowania w {dom_opieki_name} w {city_name}: ").strip()
            old_city_name = input("Podaj stare miasto, z którego pochodzi pracownik: ").strip()
            pracownik_found = False

            for pracownik in dom_opieki['players']:
                if pracownik['name'].lower() == old_pracownik_name.lower() and pracownik['city'][0].lower() == old_city_name.lower():
                    new_pracownik_name = input(f"Podaj nową nazwę dla {old_pracownik_name}: ").strip()
                    new_city_name = input("Podaj nowe miasto, z którego pochodzi zawodnik: ").strip()

                    pracownik['name'] = new_pracownik_name
                    pracownik['city'] = [new_city_name]
                    print(
                        f"Nazwa zawodnika została zmieniona z {old_pracownik_name} na {new_pracownik_name} oraz miasto z {old_city_name} na {new_city_name} w {dom_opieki_name} w {city_name}.")
                    pracownik_found = True
                    break

            if not pracownik_found:
                print(
                    f"Pracownik o nazwie {old_pracownik_name} i mieście {old_city_name} nie został znaleziony w wydarzeniu {dom_opieki_name} w {city_name}.")
            break

    if not dom_opieki_found:
        print(f"dom opieki {dom_opieki_name} w {city_name} nie zostało znalezione na liście.")


def show_pensjonariusze(domy_opieki):
    dom_opieki_name = input("Podaj nazwę domu opieki, dla którego chcesz wyświetlić listę pensjonariuszy: ").strip()
    city_name = input("Podaj miasto, w którym znajduje się dom opieki: ").strip()
    dom_opieki_found = False

    for dom_opieki in domy_opieki:
        if dom_opieki['name'].lower() == dom_opieki_name.lower() and dom_opieki['city'].lower() == city_name.lower():
            dom_opieki_found = True
            print(f"Lista pensjonariuszy dla {dom_opieki_name}, {city_name}:")
            for pensjonariusz in dom_opieki['pensjonariusze']:
                print(f" - {pensjonariusz['name']}")
            break

    if not dom_opieki_found:
        print(f"Nie znaleziono domu opieki {dom_opieki_name} w {city_name} na liście.")


def add_pensjonariusze(domy_opieki):
    dom_opieki_name = input("Podaj nazwę domu opieki, do którego chcesz dodać ppensjonariusza: ").strip()
    city_name = input("Podaj miasto, w którym odbywa się wydarzenie: ").strip()
    dom_opieki_found = False

    for dom_opieki in domy_opieki:
        if dom_opieki['name'].lower() == dom_opieki_name.lower() and dom_opieki['city'].lower() == city_name.lower():
            pensjonariusz_name = input(f"Podaj nazwę pensjonariusza do dodania do {dom_opieki_name} w {city_name}: ").strip()
            city_pensjonariusz_name = input("Podaj miasto, w którym mieszka pensjonariusz: ").strip()
            dom_opieki['pensjonariusze'].append({"name": pensjonariusz_name, "city": [city_pensjonariusz_name]})
            print(f"{pensjonariusz_name} został dodany do listy pensjonariuszy domu opieki {dom_opieki_name} w {city_name}.")
            dom_opieki_found = True
            break

    if not dom_opieki_found:
        print(f"Nie znaleziono domu opeiki {dom_opieki_name} w {city_name} na liście.")
def remove_pensjonariusze(domy_opieki):
    dom_opieki_name = input("Podaj nazwę domu opieki, z którego chcesz usunąć pensjonariusza: ").strip()
    city_name = input("Podaj miasto, w którym znajduje sie dom opieki: ").strip()
    dom_opieki_found = False

    for dom_opieki in domy_opieki:
        if dom_opieki['name'].lower() ==dom_opieki_name.lower() and dom_opieki['city'].lower() == city_name.lower():
            pensjonariusz_name = input(f"Podaj nazwę pensjonariusza do usunięcia z {dom_opieki_name} w {city_name}: ").strip()
            pensjonariusze = [pensjonariusz['name'] for pensjonariusz in dom_opieki['pensjonariusze']]
            if pensjonariusz_name in pensjonariusze:
                dom_opieki['pensjonariusze'] = [pensjonariusz for pensjonariusz in dom_opieki['pensjonariusze'] if pensjonariusz['name'] != pensjonariusz_name]
                print(f"{pensjonariusz_name} został usunięty z listy pensjonariuszy domu opieki {dom_opieki_name} w {city_name}.")
            else:
                print(f"{pensjonariusz_name} nie znaleziono na liście pensjonariuszy domu opieki {dom_opieki_name} w {city_name}.")
            dom_opieki_found = True
            break

    if not dom_opieki_found:
        print(f"Nie znaleziono wydarzenia {dom_opieki_name} w {city_name} na liście.")

def update_pensjonariusze(domy_opieki):
    dom_opieki_name = input("Podaj nazwę domu opieki, w którym chcesz zaktualizować nazwę pensjonariusza: ").strip()
    city_name = input("Podaj miasto, w którym znajduje sie dom opieki: ").strip()
    dom_opieki_found = False

    for dom_opieki in domy_opieki:
        if dom_opieki['name'].lower() == dom_opieki_name.lower() and dom_opieki['city'].lower() == city_name.lower():
            dom_opieki_found = True
            old_pensjonariusz_name = input(
                f"Podaj starą nazwę pracownika do zaktualizowania w {dom_opieki_name} w {city_name}: ").strip()
            old_city_name = input("Podaj stare miasto, zamieszkania pracownika: ").strip()
            pensjonariusz_found = False

            for pensjonariusz in dom_opieki['pensjonariusze']:
                if pensjonariusz['name'].lower() == old_pensjonariusz_name.lower() and pensjonariusz['city'][0].lower() == old_city_name.lower():
                    new_pensjonariusz_name = input(f"Podaj nową nazwę dla {old_pensjonariusz_name}: ").strip()
                    new_city_name = input("Podaj nowe miasto, zamieszkania pracownika: ").strip()

                    pensjonariusz['name'] = new_pensjonariusz_name
                    pensjonariusz['city'] = [new_city_name]
                    print(
                        f"Nazwa pracownika została zmieniona z {old_pensjonariusz_name} na {new_pensjonariusz_name} oraz miasto z {old_city_name} na {new_city_name} w {dom_opieki_name} w {city_name}.")
                    pensjonariusz_found = True
                    break

            if not pensjonariusz_found:
                print(
                    f"Pracownik o nazwie {old_pensjonariusz_name} i mieście {old_city_name} nie został znaleziony w wydarzeniu {dom_opieki_name} w {city_name}.")
            break

    if not dom_opieki_found:
        print(f"Nie znaleziono domu opieki {dom_opieki_name} w {city_name} na liście.")



def dms_to_decimal(dms):
    parts = re.split('[°′″]', dms)
    degrees = float(parts[0])
    minutes = float(parts[1]) if parts[1] else 0
    seconds = float(parts[2]) if parts[2] else 0
    decimal = degrees + (minutes / 60) + (seconds / 3600)
    return decimal

def display_map(latitude, longitude, wydarzenie, miasto):
    map_ = folium.Map(location=[latitude, longitude], zoom_start=12)
    folium.Marker([latitude, longitude], tooltip=wydarzenie).add_to(map_)
    map_file = f"{miasto}_map.html"
    map_.save(map_file)
    webbrowser.open('file://' + os.path.realpath(map_file))

def get_cords(domy_opieki):
    name = input("Podaj nazwę domu opieki, którego lokalizację chcesz wyszukać: ")
    dom_opieki_found = False
    for dom_opieki in domy_opieki:
        if dom_opieki['name'] == name:
            adres_url = f'https://pl.wikipedia.org/wiki/{dom_opieki["city"]}'
            response = requests.get(adres_url)
            response_html = BeautifulSoup(response.text, 'html.parser')

            latitude_dms = response_html.select('.latitude')[0].text
            longitude_dms = response_html.select('.longitude')[0].text

            latitude = dms_to_decimal(latitude_dms)
            longitude = dms_to_decimal(longitude_dms)

            print([latitude, longitude])
            dom_opieki_found = True
            display_map(latitude, longitude, dom_opieki['name'], dom_opieki["city"])
            return latitude, longitude
    if not dom_opieki_found:
        print(f"{name} nie znaleziono na liście")


def get_cords_pracownik(domy_opieki):
    name = input("Podaj nazwę domu opieki, którego lokalizację pracowników chcesz wyszukać: ")
    dom_opieki_found = False
    pracownik_locations = []

    for dom_opieki in domy_opieki:
        if dom_opieki['name'].lower() == name.lower():
            dom_opieki_found = True
            for pracownik in dom_opieki['pracownicy']:
                if 'city' not in pracownik or not pracownik['city']:
                    print(f"Uczestnik {pracownik['name']} nie ma podanego miasta.")
                    continue

                adres_url = f'https://pl.wikipedia.org/wiki/{pracownik["city"][0]}'
                response = requests.get(adres_url)
                response_html = BeautifulSoup(response.text, 'html.parser')

                try:
                    latitude_dms = response_html.select('.latitude')[0].text
                    longitude_dms = response_html.select('.longitude')[0].text

                    latitude = dms_to_decimal(latitude_dms)
                    longitude = dms_to_decimal(longitude_dms)

                    pracownik_locations.append((pracownik["name"], pracownik["city"][0], latitude, longitude))
                    print(f"Koordynaty pracownika {pracownik['name']}: [{latitude}, {longitude}]")
                except IndexError:
                    print(f"Koordynaty dla {pracownik['city'][0]} nie znalezione na Wikipedii.")
            break

    if dom_opieki_found and pracownik_locations:
        display_map_pracownik(pracownik_locations, name)
    elif not dom_opieki_found:
        print(f"dom opieki {name} nie został znaleziony na liście.")

def display_map_pracownik(pracownik_locations, dom_opieki_name):
    if pracownik_locations:
        avg_latitude = sum([loc[2] for loc in pracownik_locations]) / len(pracownik_locations)
        avg_longitude = sum([loc[3] for loc in pracownik_locations]) / len(pracownik_locations)
    else:
        avg_latitude = 0
        avg_longitude = 0

    map_ = folium.Map(location=[avg_latitude, avg_longitude], zoom_start=5)

    for name, city, latitude, longitude in pracownik_locations:
        folium.Marker(
            [latitude, longitude],
            tooltip=f"{name} ({city})",
            popup=f"{name} ({city})"
        ).add_to(map_)

    map_file = f"{dom_opieki_name}_player_locations_map.html"
    map_.save(map_file)
    webbrowser.open('file://' + os.path.realpath(map_file))



def get_cords_pensjonariusze(domy_opieki):
    name = input("Podaj nazwę domu opieki, której lokalizację pensjonariuszy chcesz wyszukać: ")
    dom_opieki_found = False
    pensjonariusz_locations = []
    for dom_opieki in domy_opieki:
        if dom_opieki['name'].lower() == name.lower():
            dom_opieki_found = True
            for pensjonariusz in dom_opieki['pensjonariusze']:
                if 'city' not in pensjonariusz or not pensjonariusz['city']:
                    print(f"Pensjonariusz {pensjonariusz['name']} nie ma podanego miasta.")
                    continue

                adres_url = f'https://pl.wikipedia.org/wiki/{pensjonariusz["city"][0]}'
                response = requests.get(adres_url)
                response_html = BeautifulSoup(response.text, 'html.parser')

                try:
                    latitude_dms = response_html.select('.latitude')[0].text
                    longitude_dms = response_html.select('.longitude')[0].text

                    latitude = dms_to_decimal(latitude_dms)
                    longitude = dms_to_decimal(longitude_dms)

                    pensjonariusz_locations.append((pensjonariusz["name"], pensjonariusz["city"][0], latitude, longitude))
                    print(f"Koordynaty pensjonariusza {pensjonariusz['name']}: [{latitude}, {longitude}]")
                except IndexError:
                    print(f"Koordynaty dla {pensjonariusz['city'][0]} nie znalezione na Wikipedii.")
            break

    if dom_opieki_found and pensjonariusz_locations:
        display_map_pensjonariusze(pensjonariusz_locations, name)
    elif not dom_opieki_found:
        print(f"Dom opieki {name} nie została znaleziona na liście.")


def display_map_pensjonariusze(pensjonariusz_locations, dom_opieki_name):
    if pensjonariusz_locations:
        avg_latitude = sum([loc[2] for loc in pensjonariusz_locations]) / len(pensjonariusz_locations)
        avg_longitude = sum([loc[3] for loc in pensjonariusz_locations]) / len(pensjonariusz_locations)
    else:
        avg_latitude = 0
        avg_longitude = 0

    map_ = folium.Map(location=[avg_latitude, avg_longitude], zoom_start=5)

    for name, city, latitude, longitude in pensjonariusz_locations:
        folium.Marker(
            [latitude, longitude],
            tooltip=f"{name} ({city})",
            popup=f"{name} ({city})"
        ).add_to(map_)

    map_file = f"{dom_opieki_name}_pensjonariusz_locations_map.html"
    map_.save(map_file)
    webbrowser.open('file://' + os.path.realpath(map_file))


def get_cords_all(domy_opieki):
    coordinates = []
    for dom_opieki in domy_opieki:
        adres_url = f'https://pl.wikipedia.org/wiki/{dom_opieki["city"]}'
        response = requests.get(adres_url)
        response_html = BeautifulSoup(response.text, 'html.parser')

        try:
            latitude_dms = response_html.select('.latitude')[0].text
            longitude_dms = response_html.select('.longitude')[0].text

            latitude = dms_to_decimal(latitude_dms)
            longitude = dms_to_decimal(longitude_dms)

            coordinates.append((latitude, longitude, dom_opieki["name"], dom_opieki["city"]))
            print(f'{dom_opieki["name"]} in {dom_opieki["city"]}: [{latitude}, {longitude}]')

        except (IndexError, ValueError) as e:
            print(f"Nie znaleziono dla {dom_opieki['name']} in {dom_opieki['city']}")

    if coordinates:
        display_map_all(coordinates)


def display_map_all(coordinates):
    map_ = folium.Map(location=[52.13, 19.40], zoom_start=6)
    for lat, lon, name, city in coordinates:
        folium.Marker([lat, lon], tooltip=f'{name}, {city}').add_to(map_)
    map_file = f"events_map.html"
    map_.save(map_file)
    webbrowser.open('file://' + os.path.realpath(map_file))


def dms_to_decimal_guest_all(dms_str):
    dms_regex = re.compile(
        r"(?P<degrees>-?\d+)[°\s]"
        r"(?P<minutes>\d+)?[′\s]?"
        r"(?P<seconds>\d+(\.\d+)?|)[″\s]?"
        r"(?P<direction>[NSEW])?"
    )
    match = dms_regex.match(dms_str)
    if not match:
        raise ValueError(f"Invalid DMS string: {dms_str}")
    parts = match.groupdict()
    degrees = float(parts['degrees'])
    minutes = float(parts['minutes']) if parts['minutes'] else 0
    seconds = float(parts['seconds']) if parts['seconds'] else 0
    direction = parts['direction']
    decimal = degrees + minutes / 60 + seconds / 3600
    if direction in ('S', 'W'):
        decimal = -decimal
    return decimal

def get_cords_pracownicy_all(domy_opieki):
    pracownik_locations = []

    for dom_opieki in domy_opieki:
        for pracownik in dom_opieki['pracownicy']:
            if 'city' not in pracownik or not pracownik['city']:
                print(f"Uczestnik {pracownik['name']} z domu opieki {dom_opieki['name']} nie ma podanego miasta.")
                continue

            adres_url = f'https://pl.wikipedia.org/wiki/{pracownik["city"][0]}'
            response = requests.get(adres_url)
            response_html = BeautifulSoup(response.text, 'html.parser')

            try:
                latitude_dms = response_html.select('.latitude')[0].text
                longitude_dms = response_html.select('.longitude')[0].text

                latitude = dms_to_decimal(latitude_dms)
                longitude = dms_to_decimal(longitude_dms)

                pracownik_locations.append((pracownik["name"], pracownik["city"][0], latitude, longitude, dom_opieki["name"]))
                print(f"Koordynaty pracownika {pracownik['name']} z domu opieki {dom_opieki['name']} w {pracownik['city'][0]}: [{latitude}, {longitude}]")
            except (IndexError, ValueError):
                print(f"Koordynaty dla {pracownik['city'][0]} nie znalezione lub błędne na Wikipedii.")

    if pracownik_locations:
        display_map_pracownicy_all(pracownik_locations)
    else:
        print("Nie znaleziono żadnych lokalizacji gości.")


def display_map_pracownicy_all(pracownik_locations):
    if pracownik_locations:
        avg_latitude = sum([loc[2] for loc in pracownik_locations]) / len(pracownik_locations)
        avg_longitude = sum([loc[3] for loc in pracownik_locations]) / len(pracownik_locations)
    else:
        avg_latitude = 0
        avg_longitude = 0

    map_ = folium.Map(location=[avg_latitude, avg_longitude], zoom_start=5)

    for name, city, latitude, longitude, dom_opieki in pracownik_locations:
        folium.Marker(
            [latitude, longitude],
            tooltip=f"{name} ({city})",
            popup=f"{name} ({city}) - {dom_opieki}"
        ).add_to(map_)

    map_file = f"all_player_locations_map.html"
    map_.save(map_file)
    webbrowser.open('file://' + os.path.realpath(map_file))



def dms_to_decimal_pensjonariusze_all(dms_str):
    dms_regex = re.compile(
        r"(?P<degrees>-?\d+)[°\s]"
        r"(?P<minutes>\d+)?[′\s]?"
        r"(?P<seconds>\d+(\.\d+)?|)[″\s]?"
        r"(?P<direction>[NSEW])?"
    )
    match = dms_regex.match(dms_str)
    if not match:
        raise ValueError(f"Invalid DMS string: {dms_str}")
    parts = match.groupdict()
    degrees = float(parts['degrees'])
    minutes = float(parts['minutes']) if parts['minutes'] else 0
    seconds = float(parts['seconds']) if parts['seconds'] else 0
    direction = parts['direction']
    decimal = degrees + minutes / 60 + seconds / 3600

    if direction in ('S', 'W'):
        decimal = -decimal
    return decimal


def get_cords_pensjonariusze_all(domy_opieki):
    pensjonariusz_locations = []

    for dom_opieki in domy_opieki:
        for pensjonariusz in dom_opieki['pensjonariusze']:
            if 'city' not in pensjonariusz or not pensjonariusz['city']:
                print(f"Pensjonariusz {pensjonariusz['name']} z wydarzenia {dom_opieki['name']} nie ma podanego miasta.")
                continue

            adres_url = f'https://pl.wikipedia.org/wiki/{pensjonariusz["city"][0]}'
            response = requests.get(adres_url)
            response_html = BeautifulSoup(response.text, 'html.parser')

            try:
                latitude_dms = response_html.select('.latitude')[0].text
                longitude_dms = response_html.select('.longitude')[0].text

                latitude = dms_to_decimal(latitude_dms)
                longitude = dms_to_decimal(longitude_dms)

                pensjonariusz_locations.append((pensjonariusz["name"], pensjonariusz["city"][0], latitude, longitude, dom_opieki["name"]))
                print(f"Koordynaty pracownika {pensjonariusz['name']} z firmy {dom_opieki['name']} w {pensjonariusz['city'][0]}: [{latitude}, {longitude}]")
            except (IndexError, ValueError):
                print(f"Koordynaty dla {pensjonariusz['city'][0]} nie znalezione lub błędne na Wikipedii.")

    if pensjonariusz_locations:
        display_map_pensjonariusze_all(pensjonariusz_locations)
    else:
        print("Nie znaleziono żadnych lokalizacji pensjonariuszy.")


def display_map_pensjonariusze_all(pensjonariusz_locations):
    if pensjonariusz_locations:
        avg_latitude = sum([loc[2] for loc in pensjonariusz_locations]) / len(pensjonariusz_locations)
        avg_longitude = sum([loc[3] for loc in pensjonariusz_locations]) / len(pensjonariusz_locations)
    else:
        avg_latitude = 0
        avg_longitude = 0

    map_ = folium.Map(location=[avg_latitude, avg_longitude], zoom_start=5)


    for name, city, latitude, longitude, dom_opieki in pensjonariusz_locations:
        folium.Marker(
            [latitude, longitude],
            tooltip=f"{name} ({city})",
            popup=f"{name} ({city}) - {dom_opieki}"
        ).add_to(map_)


    map_file = f"all_pensjonariusze_locations_map.html"
    map_.save(map_file)

    webbrowser.open('file://' + os.path.realpath(map_file))



correct_password = "1"
logged_in = False

while not logged_in:
    password = input('Enter your password: ')
    if password == correct_password:
        print("Zalogowany")
        logged_in = True
    else:
        print("Niepoprawne hasło")

# Główny Program
if logged_in:
        print("Witaj!")
        while True:
            print("Menu:")
            print("0. Zakończ program")
            print("1. Zarządzaj domami opieki")
            print("2. Zarządzaj pracownikami")
            print("3. Zarządzaj penjonariuszami ")
            menu_option = input("Wybierz dostępną funkcję z menu: ")
            if menu_option == '0':
                break
            elif menu_option == '1':
                while True:
                    print("0. Powrót do głównego menu")
                    print("1. Wyświetl obecną domów opieki")
                    print("2. Dodaj dom opieki do listy")
                    print("3. Usuń dom opieki z listy")
                    print("4. Aktualizuj nazwę domu opieki")
                    print("5. Wyświetl współrzędne i mapę domu opieki")
                    print("6. Wyświetl współrzędne i mapę wszystkich domów opieki")
                    dzialanie = input("Jakie działanie chcesz podjąć?: ")
                    if dzialanie == '0':
                        break
                    elif dzialanie == '1':
                        show_list(domy_opieki)
                    elif dzialanie == '2':
                        add_dom_opieki(domy_opieki)
                    elif dzialanie == '3':
                        remove_dom_opieki(domy_opieki)
                    elif dzialanie == '4':
                        update_dom_opieki(domy_opieki)
                    elif dzialanie == '5':
                        get_cords(domy_opieki)
                    elif dzialanie == '6':
                        get_cords_all(domy_opieki)
                    else:
                        print("Nieprawidłowa opcja, spróbuj ponownie.")
            elif menu_option == '2':
                while True:
                    print("0. Powrót do głównego menu")
                    print("1. Wyświetl listę uczestników danego domu opieki")
                    print("2. Dodaj pracownika")
                    print("3. Usuń pracownika")
                    print("4. Aktualizuj pracownika")
                    print("5. Wyświetl współrzędne miejsca zamieszkania pracowników")
                    print("6. Wyświetl współrzędne miejsca zamieszkania pracowników ze wszystkich wydarzeń")
                    dzialanie = input("Jakie działanie chcesz podjąć?: ")
                    if dzialanie == '0':
                        break
                    elif dzialanie == '1':
                        show_pracownicy(domy_opieki)
                    elif dzialanie == '2':
                        add_pracownik(domy_opieki)
                    elif dzialanie == '3':
                        remove_pracownicy(domy_opieki)
                    elif dzialanie == '4':
                        update_pracownicy(domy_opieki)
                    elif dzialanie == '5':
                        get_cords_pracownik(domy_opieki)
                    elif dzialanie == '6':
                        get_cords_pracownicy_all(domy_opieki)
                    else:
                        print("Nieprawidłowa opcja, spróbuj ponownie.")
            elif menu_option == '3':
                while True:
                    print("0. Powrót do głównego menu")
                    print("1. Wyświetl obecną listę pensjonariuszy dla domu opieki")
                    print("2. Dodaj pensjonariusza do listy")
                    print("3. Usuń pensjonariusza z listy")
                    print("4. Aktualizuj pensjonariusza na liście")
                    print("5. Wyświetl lokalizacje miejsca zamieszkania pensjonariuszy")
                    print("6. Wyświetl lokalizacje miejsca zamieszkania pensjonariuszy ze wszystkich domów opieki")
                    dzialanie = input("Jakie działanie chcesz podjąć?: ")
                    if dzialanie == '0':
                        break
                    elif dzialanie == '1':
                        show_pensjonariusze(domy_opieki)
                    elif dzialanie == '2':
                        add_pensjonariusze(domy_opieki)
                    elif dzialanie == '3':
                        remove_pensjonariusze(domy_opieki)
                    elif dzialanie == '4':
                        update_pensjonariusze(domy_opieki)
                    elif dzialanie == '5':
                        get_cords_pensjonariusze(domy_opieki)
                    elif dzialanie == '6':
                        get_cords_pensjonariusze_all(domy_opieki)
                    else:
                        print("Nieprawidłowa opcja, spróbuj ponownie.")