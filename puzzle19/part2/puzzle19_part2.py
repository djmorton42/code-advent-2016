from elf import Elf

NUMBER_OF_ELVES = 3018458
#NUMBER_OF_ELVES = 5

elves = []

def get_elf_accross_the_circle_index(index):
    return (index + (len(elves) / 2)) % len(elves)

for elf_index in range(NUMBER_OF_ELVES):
    elves.append(Elf(elf_index + 1))

elf_index = 0

while len(elves) > 1:
    if (len(elves) % 1000) == 0:
        print str(len(elves)) + " elves remaining..."
    
    source_elf = elves[elf_index]
    target_elf_index = get_elf_accross_the_circle_index(elf_index)
    target_elf = elves[target_elf_index]

    source_elf.take_presents_from(target_elf)
    del elves[target_elf_index]

    if target_elf_index > elf_index:
        elf_index += 1
    
    elf_index = elf_index % len(elves)

print "Elf " + str(elves[0].elf_index) + " has all the presents!"
