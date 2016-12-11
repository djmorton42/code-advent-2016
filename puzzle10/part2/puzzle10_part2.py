import re
from bot import Bot
from output_bin import OutputBin
from solution_monitor import SolutionMonitor

bot_map = {}
output_bin = {}
end_condition_bot = None

TAKE_CHIP_PATTERN = re.compile('value ([0-9]+) goes to bot ([0-9]+)')
GIVE_CHIP_PATTERN = re.compile('bot ([0-9]+) gives low to (bot|output) ([0-9]+) and high to (bot|output) ([0-9]+)')

SOLUTION_MONITOR = SolutionMonitor([17, 61])

take_chip_matches = []

def process_rules():
    global end_condition_bot
   
    gave_any = False
   
    for bot_id, bot in bot_map.items():
        result = bot.give_chips()
        if result == True:
            if gave_any == False:
                gave_any = True

            for downstream_bot in bot.get_downstream_bots():
                if downstream_bot.responsible_for(END_CONDITION_LIST) == True:
                    print "Found End Condition!!!"
                    end_condition_bot = downstream_bot.id

    if gave_any == True:
        process_rules()

def handle_take_chip(match):
    chip_value = int(match.group(1))
    bot_id = int(match.group(2))

    bot = ensure_bot_exists(bot_id)
    bot.add_chip(chip_value)

    print "Bot " + str(bot_id) + " takes chip " + str(chip_value)

def handle_give_chip(match):
    object_bot_id = int(match.group(1))
    low_subject = fetch_target(match.group(2), int(match.group(3)))
    high_subject = fetch_target(match.group(4), int(match.group(5)))

    object_bot = ensure_bot_exists(object_bot_id)

    object_bot.set_give_high_rule(high_subject)
    object_bot.set_give_low_rule(low_subject)

def fetch_target(type, id):
    if type == 'bot':
        ensure_bot_exists(id)
        return bot_map[id]
    elif type == 'output':
        ensure_output_bin_exists(id)
        return output_bin[id]
    else:
        print "Invalid Target Type: " + type

def ensure_bot_exists(id):
    if id not in bot_map:
        bot_map[id] = Bot(id, SOLUTION_MONITOR)

    return bot_map[id]

def ensure_output_bin_exists(id):
    if id not in output_bin:
        output_bin[id] = OutputBin(id)

    return output_bin[id]

with open('input.txt') as file_handle:
    for instruction in file_handle:
        give_chip_match = GIVE_CHIP_PATTERN.search(instruction) 

        if give_chip_match is not None:
            handle_give_chip(give_chip_match)
            continue
        else:
            take_chip_matches.append(TAKE_CHIP_PATTERN.search(instruction))

    for match in take_chip_matches:
        handle_take_chip(match)        

    SOLUTION_MONITOR.print_solution()
   
    output_bin_values_multiplied = (
        output_bin[0].get_chip_values()[0] * 
        output_bin[1].get_chip_values()[0] * 
        output_bin[2].get_chip_values()[0]
    )

    print "Value from first 3 output bins multiplied together: " + str(output_bin_values_multiplied)
    




