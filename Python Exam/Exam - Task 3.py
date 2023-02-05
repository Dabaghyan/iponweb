class Passenger:
    def __init__(self, name, city, rooms: dict):
        self.name = name
        self.city = city
        self.rooms = rooms

    def __repr__(self):
        return '{}, {}, {}'.format(self.name, self.city, self.rooms)

    @property
    def get_name(self):
        return self.name

    @property
    def get_city(self):
        return self.city

    @property
    def get_rooms(self):
        return self.rooms


class Hotel:
    def __init__(self, city, rooms: dict):
        self.city = city
        self.rooms = rooms

    def __repr__(self):
        return '{}, {}'.format(self.city, self.rooms)

    @property
    def get_city(self):
        return self.city

    def free_rooms_list(self, room_type):
        return self.rooms[room_type]

    def reserve_room(self, room_type, room_quantity):
        if room_type in self.rooms.keys() and self.rooms[room_type] >= room_quantity:
            self.rooms[room_type] -= room_quantity

        else:
            print("There are no free rooms of that amount")


def usage(p: Passenger, h: Hotel):
    print(p)
    print(h)
    print(p.get_city)
    print(p.name)
    print(p.rooms)
    print(h.get_city)
    print("There are {} free double rooms".format(h.free_rooms_list("Double")))
    print("There are {} free single rooms".format(h.free_rooms_list("Single")))
    print("There are {} free penthouse rooms".format(h.free_rooms_list("Penthouse")))
    h.reserve_room("Double", 3)
    print(h.rooms)
    h.reserve_room("Single", 4)
    print(h.rooms)
    h.reserve_room("Penthouse", 11)
    print(h.rooms)



p = Passenger("John Doe", "Paris", {"Double": 3})
h = Hotel("Paris", {"Double": 30, "Single": 20, "Penthouse": 10})

usage(p, h)



