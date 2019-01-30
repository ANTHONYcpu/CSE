world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's Room",
        'DESCRIPTION': "This is the classroom you ar in right now. There are two doors on the north wall.",
        'PATHS': {
            'NORTH': "PARKING_LOT"

        }
    },
    'PARKING_LOT': {
        'NAME': "The North Parking Lot",
        'DESCRIPTION': "There are a couple cars parked here",
        'PATHS': {
            'SOUTH': 'P19A'

        }
    }
}
# Controller
playing = True
current_node = world_map['R19A']
while playing:
    print(current_node['NAME']