vowels = ['a', 'e', 'i', 'o', 'u']
bad_sequences = ['ab', 'cd', 'pq', 'xy']


def is_nice_p1(given_string):
    vowel_count = sum([given_string.count(vowel) for vowel in vowels])
    if vowel_count < 3:
        print('Too less vowels!')
        return False
    double_char_counts = [
        given_string.count(char + char)
        for char in given_string
    ]
    double_char_counts = list(filter(lambda x: x > 0, double_char_counts))
    double_char_count = len(double_char_counts)
    if double_char_count <= 0:
        print('Too less double-chars!')
        return False
    for bad_sequence in bad_sequences:
        if bad_sequence in given_string:
            print('Bad sequence in string!')
            return False
    return True


def is_nice_p2(given_string):
    c1, c2 = False, False
    for index, char in enumerate(given_string):
        if len(given_string) >= index + 2:
            # first condition
            pair = char + given_string[index + 1]
            if given_string.count(pair) >= 2:
                c1 = True
            # second condition
            if index != 0:
                tri = given_string[index - 1] + char + given_string[index + 1]
                if tri[0] == tri[-1]:
                    c2 = True
        if c1 and c2:
            break
    else:
        return False
    return True


if __name__ == '__main__':
    with open('input/05') as f:
        strings = f.readlines()
    print(len([1 for s in strings if is_nice_p2(s)]))
