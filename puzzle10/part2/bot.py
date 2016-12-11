from solution_monitor import SolutionMonitor

class Bot:
    def __init__(self, bot_id, solution_monitor):
        self.bot_id = bot_id
        self.chips = []
        self.high_target = None
        self.low_target = None
        self.solution_monitor = solution_monitor

    def set_give_high_rule(self, target):
        if self.high_target is not None:
            print "Bot already has a high target!"

        self.high_target = target

    def set_give_low_rule(self, target):
        if self.low_target is not None:
            print "Bot already has a low target!"

        self.low_target = target

    def give_chips(self):
        if self.get_chip_count() == 2:

            high_chip_value = self.pop_high_value_chip()
            low_chip_value = self.pop_low_value_chip()

            self.high_target.add_chip(high_chip_value)
            self.low_target.add_chip(low_chip_value)

            print str(self) + " gives chip " + str(high_chip_value) + " to " + str(self.high_target)
            print str(self) + " gives chip " + str(low_chip_value) + " to " + str(self.low_target)

            return True
        else:
            return False

    def get_chip_count(self):
        return len(self.chips)

    def get_state(self):
        return "Bot " + str(self.bot_id) + " " + str(self.get_chip_values())

    def add_chip(self, value):
        if len(self.chips) == 2:
            raise ValueError("Bot " + str(self.bot_id) + " already has two chips!")
        
        self.chips.append(value)

        self.solution_monitor.test_solution(self)
        
        self.give_chips()

    def pop_high_value_chip(self):
        if len(self.chips) == 0:
            print "No values to pop!"

        elif len(self.chips) == 1:
            value = self.chips[0]
            del self.chips[0]
            return value

        elif self.chips[0] > self.chips[1]:
            value = self.chips[0]
            del self.chips[0]
            return value
        
        elif self.chips[1] > self.chips[0]:
            value = self.chips[1]
            del self.chips[1]
            return value

    def pop_low_value_chip(self):
        if len(self.chips) == 0:
            print "No values to pop!"

        elif len(self.chips) == 1:
            value = self.chips[0]
            del self.chips[0]
            return value

        elif self.chips[1] > self.chips[0]:
            value = self.chips[0]
            del self.chips[0]
            return value
        
        elif self.chips[0] > self.chips[1]:
            value = self.chips[1]
            del self.chips[1]
            return value

    def get_chip_values(self):
        return sorted(self.chips)

    def responsible_for(self, chip_ids):
        return sorted(chip_ids) == sorted(self.chips)
    
    def __str__(self):
        return "Bot " + str(self.bot_id)
