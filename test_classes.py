from classes import Plane, Passenger


def test_plane_init():
    plane = Plane('Airbird88', 'YourFlight', 10, [1, 2, 4, 5, 6], [3], 4)
    assert plane.plane() == 'Airbird88'
    assert plane.carrier() == 'YourFlight'
    assert plane.gate() == 10
    assert plane.seats() == [1, 2, 4, 5, 6]
    assert plane.booked_seats() == [3]
    assert plane.b_class() == 4


def test_plane_add_seat():
    plane = Plane('Airbird88', 'YourFlight', 10, [1, 2, 4, 5, 6], [3], 4)
    plane.add_seat(3)
    assert plane.plane() == 'Airbird88'
    assert plane.carrier() == 'YourFlight'
    assert plane.gate() == 10
    assert plane.seats() == [1, 2, 3, 4, 5, 6]
    assert plane.booked_seats() == []
    assert plane.b_class() == 4


def test_plane_remove_seat():
    plane = Plane('Airbird88', 'YourFlight', 10, [1, 2, 4, 5, 6], [3], 4)
    plane.remove_seat(4)
    assert plane.plane() == 'Airbird88'
    assert plane.carrier() == 'YourFlight'
    assert plane.gate() == 10
    assert plane.seats() == [1, 2, 5, 6]
    assert plane.booked_seats() == [3, 4]
    assert plane.b_class() == 4


def test_passenger_init():
    passenger = Passenger({'name': 'Jan Kwiatkowski', 'flights': [{'plane': 'Airbird88', 'seat': 3}]})
    assert passenger.name() == 'Jan Kwiatkowski'
    assert passenger.flights()[0]['plane'] == 'Airbird88'
    assert passenger.flights()[0]['seat'] == 3


def test_passenger_add_flight():
    passenger = Passenger({'name': 'Jan Kwiatkowski', 'flights': [{'plane': 'Airbird88', 'seat': 3}]})
    passenger.add_flight({'plane': 'Airbird13', 'seat': 5})
    assert passenger.name() == 'Jan Kwiatkowski'
    assert passenger.flights()[1]['plane'] == 'Airbird13'
    assert passenger.flights()[1]['seat'] == 5


def test_passenger_remove_flight():
    passenger = Passenger({'name': 'Jan Kwiatkowski', 'flights': [{'plane': 'Airbird88', 'seat': 3}]})
    passenger.remove_flight({'plane': 'Airbird88', 'seat': 3})
    assert passenger.name() == 'Jan Kwiatkowski'
    assert not passenger.flights()
