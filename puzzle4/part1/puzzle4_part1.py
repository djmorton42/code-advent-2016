from room import Room

with open('input.txt') as file_handle:
    candidate_rooms = file_handle.readlines()

    sector_id_sum = 0
    for candidate_room in candidate_rooms:
        room = Room(candidate_room)

        if room.checksum == room.calculate_checksum():
            sector_id_sum += room.sector_id

    print "Sum of sector Ids: " + str(sector_id_sum)
