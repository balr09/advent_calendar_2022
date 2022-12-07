FILENAME = 'inputs/input06.txt'


def find_different_chars(size, line):
    for c in range(len(line) - size):
        repeated = _check_x_chars(size, line[c:c + size])  # _check_4_chars(line[c:c+4])
        if not repeated:
            found = c + size
            break
    return found


def advent06_01():
    size = 4
    with open(FILENAME, 'r') as f:
        line = f.readline().strip()
        found = find_different_chars(size, line)

    return found


def advent06_02():
    size = 14
    with open(FILENAME, 'r') as f:
        line = f.readline().strip()
        found = find_different_chars(size, line)

    return found


# helpers
def _check_x_chars(l, chars):
    for i in range(l-1):
        for j in range(i+1, l):
            if chars[i] == chars[j]:
                return True
    return False
