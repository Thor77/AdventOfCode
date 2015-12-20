from re import findall, finditer, sub
from string import ascii_lowercase

forbidden_chars = ['i', 'o', 'l']


def next_char(char):
    return ascii_lowercase[
            (ascii_lowercase.index(char.lower()) + 1) % len(ascii_lowercase)]


def next_password(password):
    return sub(r'([a-y])(z*)$',
               lambda x: next_char(x.group(1)) + len(x.group(2)) * 'a', password)


def is_valid(password):
    # not contain letters
    if len([1 for c in forbidden_chars if c in password]) > 0:
        return False

    pairs = len(findall(r'([a-z])\1', password)) >= 2
    if not pairs:
        return False
    increasing_straight = False
    for index, char in enumerate(password):
        if len(password) <= index + 2:
            continue
        after_char = next_char(char)
        after_after_char = next_char(after_char)
        if (char == 'z' and after_char == 'a') or \
                (after_char == 'z' and after_after_char == 'a'):
            continue
        if password[index + 1] == after_char and password[index + 2] == after_after_char:
            return True

if __name__ == '__main__':
    with open('input/11') as f:
        password = f.read().rstrip('\n')
    while not is_valid(password):
        password = next_password(password)
    print(password)
