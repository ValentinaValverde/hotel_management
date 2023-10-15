hotel = {
    1: {
        185: ['George Jefferson', 'Wheezy Jefferson'],
    },
    2: {
        237: ['Jack Torrance', 'Wendy Torrance'],
    },
    3: {
        333: ['Neo', 'Trinity', 'Morpheus']
    }
}

while len(hotel) > 0 and len(hotel) < 10:

    user_name = input("please type your name: ")
    floor_num = int(input("please type your floor number: "))
    room_num = int(input("please type your room number: "))
    checking = input("are you checking in or out? please type 'in' for check-in and 'out' for check-out. -> ")


    new_entry = {
        floor_num: {
            room_num: [user_name]
        }
    }


    def in_or_out():
        if checking == "in":
            hotel.update(new_entry)
            print_hotel_list()

        elif checking == "out":
            del hotel[floor_num]
            print_hotel_list()
        
        else:
            print(" ")
            print("please type in or out.")
            print(" ")


    def print_hotel_list():
        print(" ")
        print("hotel list:")
        print(hotel)
        print(" ")


    if floor_num > 5:
        print("sorry, that floor level does not exist. goodbye!")
        break

    #i want to make it so that if it exists in the list, they can ONLY check out
    for x in hotel: #note that x stands for floor_num
        for y in x:  #note that y stands for room_num
            if y in x:
                print("mama mia.")


    in_or_out()
    print("new entry: ", new_entry)
    print(" ")


