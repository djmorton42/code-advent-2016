import re
from operator import itemgetter

rules = []

PATTERN = re.compile('([0-9]+)-([0-9]+)')

with open('input.txt') as file_handle:
    for rule_text in file_handle:

        match = PATTERN.match(rule_text)
        if match is None:
            print "Error!  Line " + rule_text + " didn't match the expected pattern!"
        else:
            rules.append(
                (int(match.group(1)), int(match.group(2)))
            )

rules = sorted(rules, key = itemgetter(0))

test_ip = 0

while test_ip <= 2**32:
    if (test_ip % 50000) == 0:
        print "Processing IP: " + str(test_ip)

    is_blocked = False
    for rule in rules:
        if test_ip >= rule[0] and test_ip <= rule[1] in rule:
            is_blocked = True
            break
        elif test_ip < rule[0]:
            break
    
    if not is_blocked:
        print "Found open IP: " + str(test_ip)
        break

    test_ip += 1
