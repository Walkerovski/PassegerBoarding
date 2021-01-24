from fpdf import FPDF


class Plane:
    def __init__(self, plane, carrier, gate, seats, booked_seats, b_class):
        '''
        Tworzy objekt klasy Plane, przypisuje wartosci podane w inicie.
        '''
        self._plane = plane
        self._carrier = carrier
        self._gate = gate
        self._seats = seats
        self._booked_seats = booked_seats
        self._b_class = b_class

    def add_seat(self, seat):
        '''
        Przenosi miejsce z 'zajetych' do 'wolnych' w ramach jednego obiektu.
        Innymi slowy miejsce sie zwalnia.
        '''
        self._seats.append(seat)
        self._seats.sort()
        self._booked_seats.remove(seat)

    def remove_seat(self, seat):
        '''
        Przenosi miejsce z 'wolnych' do 'zajetych' w ramach jednego obiektu.
        Innymi slowy miejsce staje sie zajete.
        '''
        self._seats.remove(seat)
        self._booked_seats.append(seat)

    def plane(self):
        '''
        zwrace nazwe obiektu(samolotu).
        '''
        return self._plane

    def carrier(self):
        '''
        zwrace przewoznika samolotu.
        '''
        return self._carrier

    def gate(self):
        '''
        zwrace bramke samolotu.
        '''
        return self._gate

    def seats(self):
        '''
        zwraca liste wolnych miejsc.
        '''
        return self._seats

    def booked_seats(self):
        '''
        zwraca liste zajetych miejsc.
        '''
        return self._booked_seats

    def b_class(self):
        '''
        zwraca miejsce od ktorego zaczynaja sie miejsca klasy premium.
        '''
        return self._b_class


class Passenger():
    def __init__(self, dictionary_of_passengers):
        '''
        Tworzy objekt klasy Passenger, przypisuje wartosci podane w inicie -
        imie pasazera oraz jego loty.
        '''
        self._name = dictionary_of_passengers["name"]
        self._flights = dictionary_of_passengers["flights"]

    def add_flight(self, flight):
        '''
        Dodaje obiektowi(pasazerowi) przelot.
        '''
        self._flights.append(flight)

    def remove_flight(self, flight):
        '''
        Usuwa obiektowi(pasazerowi) przelot.
        '''
        self._flights.remove(flight)

    def name(self):
        '''
        Zwraca imie pasazera.
        '''
        return self._name

    def flights(self):
        '''
        Zwraca liste przelotow pasazera.
        '''
        return self._flights


class PDF(FPDF):
    def lines(self):
        '''
        Tworzy ramke pdfu.
        '''
        self.rect(5.0, 5.0, 200.0, 287.0)
        self.rect(8.0, 8.0, 194.0, 282.0)

    def imagex(self):
        '''
        Ustawia grafiki w pdfie.
        '''
        self.set_xy(25, 25)
        self.image('https://i.pinimg.com/originals/1d/b0/96/1db09665876af52fa79b6a4b7429c9f3.png',  link='', type='', w=40, h=40)
        self.set_xy(145, 25)
        self.image('https://i.pinimg.com/originals/1d/b0/96/1db09665876af52fa79b6a4b7429c9f3.png',  link='', type='', w=40, h=40)
        self.set_xy(25, 235)
        self.image('https://i.pinimg.com/originals/1d/b0/96/1db09665876af52fa79b6a4b7429c9f3.png',  link='', type='', w=40, h=40)
        self.set_xy(145, 235)
        self.image('https://i.pinimg.com/originals/1d/b0/96/1db09665876af52fa79b6a4b7429c9f3.png',  link='', type='', w=40, h=40)

    def texts(self, passenger, plane, seat):
        '''
        Wypelnia pdf danymi.
        '''
        self.set_font('Arial', '', 16)
        x = 65
        y = 100
        self.set_xy(x, y)
        self.cell(w=10, h=10.0, txt="Dane pasazera:", border=0)
        y = y + 16
        self.set_xy(x, y)
        self.cell(w=10, h=10.0, txt="Imie i nazwisko:", border=0)
        self.set_xy(x + 47, y)
        self.cell(w=10, h=10.0, txt=passenger.name(), border=0)
        y = y + 16
        self.set_xy(x, y)
        self.cell(w=10, h=10.0, txt="Szczegoly lotu:", border=0)
        y = y + 16
        self.set_xy(x, y)
        self.cell(w=10, h=10.0, txt="Samolot:", border=0)
        self.set_xy(x + 47, y)
        self.cell(w=10, h=10.0, txt=plane.plane(), border=0)
        y = y + 8
        self.set_xy(x, y)
        self.cell(w=10, h=10.0, txt="Przewoznik:", border=0)
        self.set_xy(x + 47, y)
        self.cell(w=10, h=10.0, txt=plane.carrier(), border=0)
        y = y + 8
        self.set_xy(x, y)
        self.cell(w=10, h=10.0, txt="Bramka:", border=0)
        self.set_xy(x + 47, y)
        self.cell(w=10, h=10.0, txt=str(plane.gate()), border=0)
        y = y + 8
        self.set_xy(x, y)
        self.cell(w=10, h=10.0, txt="Miejsce numer:", border=0)
        self.set_xy(x + 47, y)
        self.cell(w=10, h=10.0, txt=str(seat), border=0)
        y = y + 8
        self.set_xy(x, y)
        self.cell(w=10, h=10.0, txt="Klasa:", border=0)
        self.set_xy(x + 47, y)
        if int(seat) >= plane.b_class():
            self.cell(w=10, h=10.0, txt='biznesowa', border=0)
        else:
            self.cell(w=10, h=10.0, txt='ekonomiczna', border=0)
