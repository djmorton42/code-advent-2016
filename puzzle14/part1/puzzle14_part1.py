import md5

SALT = 'jlmsuwbz'
#SALT = 'abc'

keys = []

index = 0

candidate_key_list = []

def get_triplet(candidate_key):
    for i in range(len(candidate_key) - 2):
        if candidate_key[i] == candidate_key[i + 1] and candidate_key[i] == candidate_key[i + 2]:
            return candidate_key[i:i + 3]

    return None

def generate_candidate_key_for_index(index):
    return md5.new(SALT + str(index)).hexdigest().lower()

def get_candidate_key_for_index(index):
    if index < len(candidate_key_list):
        return candidate_key_list[index]
    else:
        candidate_key_list.append(generate_candidate_key_for_index(index))
        return candidate_key_list[index]

while len(keys) < 64:
    candidate_key = get_candidate_key_for_index(index) 

    triplet = get_triplet(candidate_key)

    if triplet is not None:
        for i in range(1000):
            if (triplet[0] * 5 in get_candidate_key_for_index(index + i + 1)):
                keys.append(candidate_key)
                break

    index += 1
    
print "Final Index: " +  str(index - 1)
