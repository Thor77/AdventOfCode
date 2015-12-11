from hashlib import md5

with open('input/04') as f:
    start = f.read().rstrip('\n')
counter = 0
hashed = ''
while not hashed.startswith('000000'):
    counter += 1
    m = md5()
    m.update((start + str(counter)).encode())
    hashed = m.hexdigest()
print('Solution:', counter, 'MD5', hashed)
