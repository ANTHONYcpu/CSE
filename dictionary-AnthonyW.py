world_map = {
    'R19A': {
        'NAME': "NBA 2K LOGO",
        'DESCRIPTION': "THIS IS WERE YOU START FORM.",
        'PATHS': {
            'NORTH': "THE NEIGHBORHOOD"
        }
    },
    'PARKING_LOT': {
        'NAME': "NBA 2K COURTS",
        'DESCRIPTION': "THERE IS OTHER PLAYERS PLAYING ON THE NBA 2K COURTS.",
        'PATHS': {
            'SOUTH': 'NBA 2K 3s COURTS'
        }
    },
    'PARKING_LOT2': {
        'NAME': "NBA 2K I GOT NEXT SPOT",
        'DESCRIPTION': "WHEN YOU HOP ON THE SPOT YOU WAIT TO GET INTO A GAME .",
        'PATHS': {
            'SOUTH': 'THERE ARE OTHERS COURTS'
        }
    }
}



# Other Variables

directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]

current_node = world_map["R19A"]  # This is your current location

playing = True



# Controller

while playing:

    print(current_node['NAME'])



    command = input(">_")

    if command.lower() in ['q', 'quit', 'exit']:

        playing = False

    elif command in directions:

        try:

            room_name = current_node["PATHS"][command]

            current_node = world_map[room_name]

        except KeyError:

            print("I can't go that way.")

    else:

        print("Command not recognized.")