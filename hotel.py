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

def some_function():
    if checking == "in":
        hotel.update(floor)
        print(hotel)
    elif checking == "out":
        del hotel[floor_num]
        print(hotel)


def main_function():
    print("this is running!")

    if floor_num == 1 and room_num == 185:
        some_function()
    elif floor_num == 2 and room_num == 237:
        some_function() 
    elif floor_num == 3 and room_num == 333:
        some_function()
    else:
        some_function()


# new_list = [] 
# new_list.append(user_name, floor_num, room_num)   
# print(new_list)

main_function()