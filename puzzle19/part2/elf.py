class Elf:
    def __init__(self, elf_index):
        self.number_of_presents = 1
        self.elf_index = elf_index

    def take_presents_from(self, elf):
        number_of_presents = elf.number_of_presents
        self.number_of_presents += number_of_presents
        elf.number_of_presents -= number_of_presents

