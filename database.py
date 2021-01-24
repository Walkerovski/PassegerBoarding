import json
from classes import Passenger, Plane


def read_from_file():
    '''
    Zamienia bazy danych (jsony) w obiekty klas Passenger oraz Plane.
    '''
    with open('passengers.json') as file_passengers:
        data = json.load(file_passengers)
        passengers = []
        for item in data:
            person = Passenger(item)
            passengers.append(person)
    with open('planes.json') as file_planes:
        data = json.load(file_planes)
        planes = []
        for item in data:
            plane = Plane(
                item['plane'],
                item['carrier'],
                item['gate'],
                item['seats'],
                item['booked_seats'],
                item['b_class']
            )
            planes.append(plane)
    return passengers, planes
