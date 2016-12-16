INITIAL_STATE = '01110110101001000'
DISK_SIZE = 272

def calculate_checksum(value_to_check):
    output = ''

    for i in xrange(0, len(value_to_check), 2):
        candidate_pair = value_to_check[i:i + 2]
        output += '1' if candidate_pair[0] == candidate_pair[1] else '0'

    if len(output) % 2 == 0:
        return calculate_checksum(output)
    else:
        return output

def expand_data(data):
    intermediate_value = data[::-1].replace('1', 'X').replace('0', '1').replace('X', '0')
    return data + '0' + intermediate_value 

data = INITIAL_STATE

while len(data) < DISK_SIZE:
    data = expand_data(data)

data = data[0:DISK_SIZE]

print 'Checksum: ' + calculate_checksum(data)
