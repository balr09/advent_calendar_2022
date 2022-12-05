def advent01_01():
    maxfood = 0
    current_food = 0
    with open('inputs/input01.txt', 'r') as f:
        for line in f:
            if len(line.strip()) == 0:
                if current_food > maxfood:
                    maxfood = current_food

                # print('end -- mx: %d -- current: %d' % (maxfood, current_food))
                current_food = 0
            else:
                current_food += int(line)

    if current_food > maxfood:
        maxfood = current_food
    return maxfood


def advent01_02():
    foods = list()
    current_food = 0
    with open('inputs/input01.txt', 'r') as f:
        for line in f:
            if len(line.strip()) == 0:
                foods.append(current_food)
                current_food = 0
            else:
                current_food += int(line)

    foods.sort(reverse=True)
    maxfood = 0
    for i in range(min(3, len(foods))):
        maxfood += foods[i]

    return maxfood

