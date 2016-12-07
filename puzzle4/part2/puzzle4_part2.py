from room import Room

with open('input.txt') as file_handle:
    candidate_rooms = file_handle.readlines()

    for candidate_room in candidate_rooms:
        room = Room(candidate_room)

        if room.checksum == room.calculate_checksum():
            print room.decrypt_name() + " => Sector Id: " + str(room.sector_id)

