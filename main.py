from classes import Passenger, PDF
from database import read_from_file


def find(planes, what):
    '''
    Zwraca szukany samolot sposrod wszystkich obiektow klasy Plane.
    '''
    for item in planes:
        if item.plane() == what:
            return item
    return ''


def find_flight(passenger, plane, seat):
    '''
    Zwraca szukany lot sposrod wszystkich lotow pasazera.
    '''
    for item in passenger.flights():
        if item['plane'] == plane and item['seat'] == seat:
            return item
    return ''


def add_flight(plane, passenger, seat):
    '''
    Dodaje lot do listy lotow pasazera.
    '''
    if seat not in plane.seats():
        print('To miejsce jest niedostepne.')
        return
    dictio = {'plane': plane.plane(), 'seat': seat}
    passenger.add_flight(dictio)
    plane.remove_seat(seat)


def login(passengers, name):
    '''
    Znajduje pasazera na liscie objektow klasy Passenger.
    '''
    for passenger in passengers:
        if passenger.name() == name:
            return passenger
    return add_passenger(passengers, name)


def add_passenger(passengers, name):
    '''
    Tworzy nowego pasazera i dodaje go do listy objektow klasy Passenger.
    '''
    new = {}
    new['name'] = name
    new['flights'] = []
    passengers.append(Passenger(new))
    return login(passengers, name)


def add_reservation(planes, passenger):
    '''
    Dodaje lot do listy lotow pasazera.
    Aktualizuje stan samolotu('zajmuje' wybrane miejsce)
    '''
    print('Dostepne samoloty:')
    for plane in planes:
        print(f'{plane.plane()}, dostepnych miejsc: {len(plane.seats())}')
    while True:
        flight = input('Prosze podac nazwe samolotu:\n')
        plane = find(planes, flight)
        if not plane:
            print('Prosze sprawdzic nazwe samolotu i wpisac ja jeszcze raz.')
        else:
            break
    print(
        f'Dostepne miejsca: {plane.seats()}',
        f'Miejsca od {plane.b_class()} naleza do klasy biznesowej',
        sep='\n'
    )
    while True:
        seat = input('Wybierz miejsce:\n')
        if seat.isdigit():
            seat = int(seat)
            if seat in plane.seats():
                break
            else:
                print('Prosze sprawdzic miejsce i wpisac je jeszcze raz.')
        else:
            print('Miejsce musi byc liczba.')
    add_flight(plane, passenger, seat)


def delete_resevation(planes, passenger):
    '''
    Usuwa lot z listy lotow pasazera.
    Aktualizuje stan samolotu('zwalnia' wybrane miejsce)
    '''
    print('Twoje przeloty:')
    for item in passenger.flights():
        print(item['plane'], item['seat'])
    while True:
        plane = input("Podaj samolotaby anulowac lot:\n")
        plane = find(planes, plane)
        if not plane:
            print('Nie ma takiego samolotu, sprawdz nazwe.')
        else:
            break
    while True:
        seat = input("Podaj miejsce aby anulowac lot:\n")
        if seat.isdigit():
            seat = int(seat)
            break
        else:
            print('Miejsce musi byc liczba.')
    your_flight = find_flight(passenger, plane.plane(), seat)
    if not your_flight:
        print('Nie jestes wlascicielem takiego przelotu.')
        return delete_resevation(planes, passenger)
    plane.add_seat(seat)
    passenger.remove_flight(your_flight)


def change_resevation(planes, passenger):
    '''
    Wyszukuje lot w liscie lotow pasazera.
    Aktualizuje miejsce w rezerwacji pasazera
    Aktualizuje stan samolotu('zwalnia' stare i 'zajmuje' nowe miejsce)
    '''
    if not passenger.flights():
        print('Brak lotow, wybierz 1 aby dokonac rezerwacji.')
        return
    print('Twoje przeloty:')
    for item in passenger.flights():
        print(item['plane'], item['seat'])
    while True:
        plane = input("Podaj samolot aby anulowac lot:\n")
        plane = find(planes, plane)
        if not plane:
            print('Nie ma takiego samolotu, sprawdz nazwe.')
        else:
            break
    while True:
        seat = input("Podaj miejsce aby anulowac lot:\n")
        if seat.isdigit():
            seat = int(seat)
            break
        else:
            print('Miejsce musi byc liczba.')
    your_flight = find_flight(passenger, plane.plane(), seat)
    if not your_flight:
        print('Nie jestes wlascicielem takiego przelotu.')
        return change_resevation(planes, passenger)
    passenger.remove_flight(your_flight)
    plane.add_seat(seat)
    print(f'Wybierz nowe miejsce:{plane.seats()}')
    while True:
        seat = input("Podaj nowe miejsce:\n")
        if seat.isdigit():
            seat = int(seat)
            break
        else:
            print('Miejsce musi byc liczba.')
    add_flight(plane, passenger, seat)


def call_advisor():
    '''
    Wyswietla nr infolini.
    '''
    print('Infolinia: +48 123 456 789')


def print_ticket(planes, passenger):
    '''
    Wyszukuje lot i przekazuje jego dane do generacji pdfa.
    '''
    print("Twoje bilety:")
    check_your_flights(planes, passenger)
    while True:
        plane = input("Podaj nazwe samolotu dla ktorego ma zostac wygenerowany bilet: ")
        plane = find(planes, plane)
        if not plane:
            print('Prosze sprawdzic nazwe samolotu i wpisac ja jeszcze raz.')
        else:
            break
    while True:
        seat = input('Podaj numer miejsca dla ktorego ma zostac wygenerowany bilet: ')
        if seat.isdigit():
            seat = int(seat)
            break
        else:
            print('Miejsce musi byc liczba.')
    your_flight = find_flight(passenger, plane.plane(), seat)
    if not your_flight:
        print('Prosze sprawdzic podane dane na bilecie i wpisac je jeszcze raz.')
        return print_ticket(planes, passenger)
    pdf = PDF()
    pdf.add_page()
    pdf.lines()
    pdf.imagex()
    pdf.texts(passenger, plane, seat)
    pdf.output('test.pdf')


def check_all_flights(planes):
    '''
    Wyswietla informacje o wszystkich lotach.
    '''
    for item in planes:
        print(
            f'Samolot: {item.plane()}',
            f'Ilosc wolnych miejsc: {len(item.seats())}',
            f'Bramka: {item.gate()}',
            f'Przewoznik: {item.carrier()}\n',
            sep='\n'
        )


def check_your_flights(planes, passenger):
    '''
    Wyswietla informacje o wszystkich lotach pasazera.
    '''
    if not passenger.flights():
        print('Brak lotow, wybierz 1 aby dokonac rezerwacji.')
    for flight in passenger.flights():
        for item in planes:
            if flight['plane'] == item.plane():
                print(
                    f'Samolot: {item.plane()}',
                    f'Miejsce: {flight["seat"]}',
                    sep='\n'
                )
                if item.b_class() <= flight["seat"]:
                    print(f'Klasa: biznesowa')
                else:
                    print(f'Klasa: ekonomiczna')
                print(
                    f'Ilosc wolnych miejsc: {len(item.seats())}',
                    f'Bramka: {item.gate()}',
                    f'Przewoznik: {item.carrier()}\n',
                    sep='\n'
                )


def menu_action(planes, passenger):
    '''
    Pozwala wybrac akcje programu.
    '''
    print(
        'Wybierz dzialanie:',
        'Wpisz 1 by dokonac rezerwacji',
        'Wpisz 2 by usunac rezerwacje',
        'Wpisz 3 by zmodyfikowac rezerwacje',
        'Wpisz 4 by sprawdzic szczegoly lotow',
        'Wpisz 5 by sprawdzic szczegoly swoich lotow',
        'Wpisz 6 by wygenerowac bilet',
        'Wpisz 7 by skontaktowac sie z konsultantem',
        'Wpisz 8 by sie wylogowac',
        sep='\n'
    )
    do = input()
    if do == '1':
        add_reservation(planes, passenger)
    elif do == '2':
        delete_resevation(planes, passenger)
    elif do == '3':
        change_resevation(planes, passenger)
    elif do == '4':
        check_all_flights(planes),
    elif do == '5':
        check_your_flights(planes, passenger),
    elif do == '6':
        print_ticket(planes, passenger),
    elif do == '7':
        call_advisor()
    elif do == '8':
        print("Wylogowano")
        return 0
    else:
        print('Prosze wpisac liczbe od 1 do 8')
    return 1


if __name__ == "__main__":
    '''
    Pobiera dane do zalogowania sie.
    '''
    passengers, planes = read_from_file()
    name = ""
    while not name:
        name = input('Podaj imie i nazwisko:\n')
    print(f'Witamy {name}!')
    passenger = login(passengers, name)
    while(menu_action(planes, passenger)):
        pass
