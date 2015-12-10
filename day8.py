with open('input/08') as f:
    raw_strings = f.readlines()

escape_sequences = {
    r'"': r'\"',
    '\\': '\\\\',
}


def memory_value_chars(raw_string):
    return len(eval(raw_string))


def extra_encoded_chars(raw_string):
    for key, value in escape_sequences.items():
        raw_string = raw_string.replace(key, value)
    return len(raw_string) + 2

if __name__ == '__main__':
    code_chars = 0
    memory_chars = 0
    encoded_chars = 0
    for raw_string in raw_strings:
        raw_string = raw_string.rstrip('\n')
        code_chars += len(raw_string)
        memory_chars += memory_value_chars(raw_string)
        encoded_chars += extra_encoded_chars(raw_string)
    # print(code_chars - memory_chars)  # part 1
    print(encoded_chars - code_chars)  # part 2
