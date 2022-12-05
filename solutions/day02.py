def advent02_01():
    result = 0
    with open('inputs/input02.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            elf, me = line.split(' ')
            punc = _punctuation01(elf, me)
            result += punc

    return result


def advent02_02():
    result = 0
    with open('inputs/input02.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            elf, me = line.split(' ')
            punc = _punctuation02(elf, me)
            result += punc

    return result


# helpers
def _punctuation02(elf, me):
    draw_value = _get_real_play_value(me)
    result = draw_value

    elf_play = _get_real_play_value(elf)
    my_play = _get_my_real_play(elf_play, draw_value)

    result += my_play
    return result


def _get_my_real_play(elf_play, draw_value):
    my_play = 0
    if draw_value == 0:
        my_play = elf_play + 2
    elif draw_value == 3:
        my_play = elf_play
    elif draw_value == 6:
        my_play = elf_play + 1

    if my_play > 3:
        my_play -= 3
    return my_play


def _get_real_play_value(play):
    if play == 'X':
        return 0
    elif play == 'A':
        return 1
    elif play == 'B':
        return 2
    elif play == 'C' or play == 'Y':
        return 3
    elif play == 'Z':
        return 6

    return 0


def _punctuation01(elf, me):
    elf_value = _get_fake_play_value(elf)
    my_value = _get_fake_play_value(me)

    diff = my_value - elf_value
    result = 0
    if diff == 1 or diff == -2:
        result = 6
    elif diff == 0:
        result = 3

    return result + my_value


def _get_fake_play_value(play):
    if play == 'X' or play == 'A':
        return 1
    elif play == 'Y' or play == 'B':
        return 2
    elif play == 'Z' or play == 'C':
        return 3

    return 0

# 0 A    0 X
# 1 B    1 Y
# 2 C    2 Z
#
#  2 - pierdo
#  1 - gano
#  0 - empate
# -1 - pierdo
# -2 - gano
