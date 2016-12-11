#from bot import Bot

class SolutionMonitor:

    def __init__(self, solution):
        self.solution = solution
        self.solution_bot_id = None

    def test_solution(self, bot):
        if bot.responsible_for(self.solution):
            self.solution_bot_id = bot.bot_id

    def print_solution(self):
        if self.solution_bot_id is None:
            print "No solution found"
        else:
            print "********"
            print "** Bot " + str(self.solution_bot_id) + " is responsible for handling chips " + str(self.solution)
            print "********"
