class Elf:
    def __init__(self, elf_index, next_elf = None):
        self.elf_index = elf_index
        self.next_elf = next_elf
        self.number_of_presents = 0

    def take_next_present(self):
        if self == self.next_elf:
            return False
        else:
            number_of_presents = self.next_elf.number_of_presents

            self.number_of_presents += number_of_presents
            self.next_elf.number_of_presents = 0
            self.next_elf = self.next_elf.next_elf
            return True
