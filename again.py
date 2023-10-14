hotel = {
    '1': {
        '185': ['George Jefferson', 'Wheezy Jefferson'],
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}


user_name = input("please type your name: ")
floor_num = input("please type your floor number: ")
room_num = input("please type your room number: ")
checking = input("are you checking in or out? please type 'in' for check-in and 'out' for check-out. -> ")


floor = {
    floor_num: {
        room_num: [user_name]
    }
}


def in_or_out():
    if checking == "in":
        hotel.update(floor)
        print(hotel)
    elif checking == "out":
        del hotel[floor_num]
        print(hotel)


def print_hotel_list():
    print(" ")
    print("hotel list:")
    print(" ")
    print(hotel)

