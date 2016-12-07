import md5

DOOR_ID = 'abbhdwsy'
password = ['-', '-', '-', '-', '-', '-', '-', '-']

counter = 0

def is_valid_hash(digest):
    return digest.startswith('00000') and ord(digest[5]) >= 48 and ord(digest[5]) <= 55

def position_is_populated(position):
    return password[position] != '-'

while '-' in password:
    digest_input = DOOR_ID + str(counter)
    digest = md5.new(digest_input).hexdigest()
   
    counter += 1

    if is_valid_hash(digest):
        position = int(digest[5])
        if not position_is_populated(position):
            password[position] = digest[6]
            print ''.join(password)
    
print "Password: " + ''.join(password)
