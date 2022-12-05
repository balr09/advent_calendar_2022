def advent03_01():
    priorities = 0
    with open('inputs/input03.txt', 'r') as f:
        for line in f:
            line = line.strip()
            middle = len(line)
            middle = int(middle / 2)
            rs1 = line[:middle]
            rs2 = line[middle:]

            # print('%d --> %s - %s' % (middle, rs1, rs2))
            viewed = ''
            for c in rs1:
                if c in rs2:
                    if c in viewed:
                        continue
                    viewed += c
                    value = _get_char_value(c)
                    # print('c %s --> v %d' % (c, value))
                    priorities += value
    return priorities


def advent03_02():
    priorities = 0
    with open('inputs/input03.txt', 'r') as f:
        l = 0
        contents = ['', '', '']
        for line in f:
            div = l % 3
            contents[div] = line
            if div == 2:
                c = _get_badge(contents)
                priorities += _get_char_value(c)

            # print('rest %d' % div)
            # last operation:
            l += 1
    return priorities

# helpers
def _get_badge(contents):
    for c in contents[0]:
        if c in contents[1] and c in contents[2]:
            return c

    return 'not_found'


def _get_char_value(c):
    base_val = int(bytes('a', 'ascii')[0])
    value = int(bytes(c, 'ascii')[0])
    value = value - base_val + 1
    if value < 0:
        value += 58

    return value