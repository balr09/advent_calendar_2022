def advent04_01():
    spares = 0
    with open('inputs/input04.txt', 'r') as f:
        for line in f:
            s1, e1, s2, e2 = _get_edges(line)
            if (s1 <= s2 and e2 <= e1) or (s2 <= s1 and e1 <= e2):
                # print(f'********* {line}')
                spares += 1

    return spares


def advent04_02():
    overlaps = 0
    with open('inputs/input04.txt', 'r') as f:
        for line in f:
            s1, e1, s2, e2 = _get_edges(line)
            int = [value for value in range(s1, e1+1) if value in range(s2, e2+1)]
            if len(int) > 0:
                overlaps += 1

    return overlaps


# helpers
def _get_edges(line):
    line = line.strip()
    sections = line.split(',')
    s1, e1 = sections[0].split('-')
    s1 = int(s1)
    e1 = int(e1)
    s2, e2 = sections[1].split('-')
    s2 = int(s2)
    e2 = int(e2)

    return s1, e1, s2, e2