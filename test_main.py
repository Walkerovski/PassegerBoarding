from classes import Plane, Passenger
from main import find, find_flight, add_flight, login, add_passenger
from main import add_reservation, delete_resevation, change_resevation
from main import check_all_flights


def test_find():
    plane = Plane('Airbird88', 'YourFlight', 10, [1, 2, 4, 5, 6], [3], 4)
    plane2 = Plane('Airbird889', 'YourFlight', 10, [1, 2, 4, 5, 6], [3], 4)
    planes = [plane, plane2]
    assert find(planes, 'Airbird889') == plane2


def test_find_flight():
    passenger = Passenger({'name': 'Jan Kwiatkowski', 'flights': [{'plane': 'Airbird88', 'seat': 3}]})
    assert find_flight(passenger, 'Airbird88', 3) == passenger.flights()[0]


def test_add_flight():
    plane = Plane('Airbird88', 'YourFlight', 10, [1, 2, 4, 5, 6], [3], 4)
    passenger = Passenger({'name': 'Jan Kwiatkowski', 'flights': []})
    add_flight(plane, passenger, 4)
    assert passenger.flights()[0] == {'plane': 'Airbird88', 'seat': 4}
    assert plane.seats() == [1, 2, 5, 6]
    assert plane.booked_seats() == [3, 4]


def test_login():
    passenger1 = Passenger({'name': 'Jan Kwiatkowski', 'flights': [{'plane': 'Airbird88', 'seat': 3}]})
    passenger2 = Passenger({'name': 'Piotr Gawkowski', 'flights': [{'plane': 'Airbird13', 'seat': 13}]})
    passengers = [passenger1, passenger2]
    assert login(passengers, 'Jan Kwiatkowski') == passenger1


def test_add_passenger():
    passengers = []
    add_passenger(passengers, 'Jan Kwiatkowski')
    assert passengers[0].name() == 'Jan Kwiatkowski'


def test_add_reservation(monkeypatch):
    plane = Plane('Airbird88', 'YourFlight', 10, [1, 2, 4, 5, 6], [3], 4)
    plane2 = Plane('Airbird889', 'YourFlight', 10, [1, 2, 4, 5, 6], [3], 4)
    planes = [plane, plane2]
    passenger = Passenger({'name': 'Jan Kwiatkowski', 'flights': [{'plane': 'Airbird88', 'seat': 3}]})
    responses = iter(['Airbird889', '4'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    add_reservation(planes, passenger)
    assert passenger.name() == 'Jan Kwiatkowski'
    assert passenger.flights()[0] == {'plane': 'Airbird88', 'seat': 3}
    assert passenger.flights()[1] == {'plane': 'Airbird889', 'seat': 4}
    assert plane2.seats() == [1, 2, 5, 6]
    assert plane2.booked_seats() == [3, 4]


def test_delete_resevation(monkeypatch):
    plane = Plane('Airbird88', 'YourFlight', 10, [1, 2, 4, 5, 6], [3], 4)
    plane2 = Plane('Airbird889', 'YourFlight', 10, [1, 2, 4, 5, 6], [3], 4)
    planes = [plane, plane2]
    passenger = Passenger({'name': 'Jan Kwiatkowski', 'flights': [{'plane': 'Airbird88', 'seat': 3}]})
    assert passenger.flights()[0] == {'plane': 'Airbird88', 'seat': 3}
    responses = iter(['Airbird88', '3'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    delete_resevation(planes, passenger)
    assert passenger.name() == 'Jan Kwiatkowski'
    assert not passenger.flights()
    assert plane.seats() == [1, 2, 3, 4, 5, 6]
    assert plane.booked_seats() == []


def test_change_resevation(monkeypatch):
    plane = Plane('Airbird88', 'YourFlight', 10, [1, 2, 4, 5, 6], [3], 4)
    plane2 = Plane('Airbird889', 'YourFlight', 10, [1, 2, 4, 5, 6], [3], 4)
    planes = [plane, plane2]
    passenger = Passenger({'name': 'Jan Kwiatkowski', 'flights': [{'plane': 'Airbird88', 'seat': 3}]})
    assert passenger.flights()[0] == {'plane': 'Airbird88', 'seat': 3}
    responses = iter(['Airbird88', '3', '1'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    change_resevation(planes, passenger)
    assert passenger.name() == 'Jan Kwiatkowski'
    assert passenger.flights()[0] == {'plane': 'Airbird88', 'seat': 1}
