from elf import Elf

NUMBER_OF_ELVES = 3018458

last_elf = None
recent_elf = None


for elf_index in range(NUMBER_OF_ELVES):
    if last_elf is None:
        recent_elf = Elf(NUMBER_OF_ELVES - elf_index)
        last_elf = recent_elf
    else:
        recent_elf = Elf(NUMBER_OF_ELVES - elf_index, recent_elf)

last_elf.next_elf = recent_elf

current_elf = recent_elf

while current_elf.take_next_present():
    current_elf = current_elf.next_elf

print "Elf " + str(current_elf.elf_index) + " has all the presents!"
