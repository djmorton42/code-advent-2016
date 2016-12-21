import re
from operator import attrgetter
from range import Range

rules = []

PATTERN = re.compile('([0-9]+)-([0-9]+)')

with open('input.txt') as file_handle:
    for rule_text in file_handle:

        match = PATTERN.match(rule_text)
        if match is None:
            print "Error!  Line " + rule_text + " didn't match the expected pattern!"
        else:
            rules.append(
                Range(int(match.group(1)), int(match.group(2)))
            )

def merge_rules(rules):
    merged_rules = []
    removed_rules = set()
    
    for rule in rules:
        if rule in removed_rules:
            continue

        merged_rules.append(rule)

        for other_rule in rules:
            if other_rule == rule or other_rule in removed_rules:
                continue

            if rule.intersects(other_rule):
                rule.union(other_rule)
                removed_rules.add(other_rule)

    return merged_rules

rules = sorted(rules, key = attrgetter('start'))

while True:
    current_number_of_rules = len(rules)
    rules = merge_rules(rules)
    if len(rules) == current_number_of_rules:
        break;
    else:
        print "Reduced number of rules from " + str(current_number_of_rules) + " to " + str(len(rules))

max_ips = 2**32

for rule in rules:
    max_ips -= rule.number_of_ips_in_range()

print "Number of IPs not blocked: " + str(max_ips)
