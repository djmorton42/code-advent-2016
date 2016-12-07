import md5

DOOR_ID = 'abbhdwsy'
password = ''

counter = 0

while len(password) < 8:
    digest_input = DOOR_ID + str(counter)
    digest = md5.new(digest_input).hexdigest()
   
    counter += 1

    if digest.startswith('00000'):
        password += digest[5]
    
print "Password: " + password
