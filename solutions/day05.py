FILENAME = 'inputs/input05.txt'


def advent05_01():
    answer = ''
    piles = _build_arrays()
    piles = _perform_operations(piles)
    # build answer
    for pile in piles:
        answer += str(pile[-1])

    return answer


def advent05_02():
    answer = ''
    piles = _build_arrays()
    piles = _perform_operations_9001(piles)
    # build answer
    for pile in piles:
        answer += str(pile[-1])

    return answer


# helpers
def _perform_operations_9001(piles):
    with open(FILENAME, 'r') as f:
        for line in f:
            if not line.startswith('move'):
                continue

            line = line.rstrip()
            move, quantity, fr, pile1, to, pile2 = line.split(' ')
            elems = list()
            for i in range(int(quantity)):
                elems.insert(0, piles[int(pile1) - 1].pop())
            for i in range(int(quantity)):
                piles[int(pile2) - 1].append(elems[i])

    return piles


def _perform_operations(piles):
    with open(FILENAME, 'r') as f:
        for line in f:
            if not line.startswith('move'):
                continue

            line = line.rstrip()
            move, quantity, fr, pile1, to, pile2 = line.split(' ')
            for i in range(int(quantity)):
                piles[int(pile2)-1].append(piles[int(pile1)-1].pop())

    return piles


def _build_arrays():
    piles = list()
    cargo_lines = list()
    numbers_line = ''
    with open(FILENAME, 'r') as f:
        for line in f:
            line = line.rstrip()
            if '[' in line:
                cargo_lines.append(line)
            elif len(line) == 0:
                break
            else:
                numbers_line = line

    cargo_lines.reverse()
    for c in numbers_line:
        if c == ' ':
            continue

        pos = numbers_line.index(c)
        c = int(c)
        # print(f'{c} - {pos}')
        new_pile = list()
        for cl in cargo_lines:
            if pos < len(cl) and len(cl[pos].strip()) > 0:
                new_pile.append(cl[pos])

        piles.append(new_pile)
        # print(f'{new_pile}')

    return piles