
with open("day1input.txt") as input_list:
    x = input_list.read().splitlines()
    newx = [int(a) for a in x]

    # print(newx)

sum_x = 2020
incomplete = True

while incomplete:
    for index, var_a in enumerate(newx):
        if not incomplete:
            break
        for var_b in newx[(index+1):]:
            if not incomplete:
                break
            for var_c in newx[(index+2):]:
                if (var_a + var_b + var_c) == sum_x:
                    print(
                        f'variable a is:{var_a},variable b is:{var_b}, and variable c is:{var_c}. Multiplied against each other results in:{var_a * var_b * var_c}')
                    incomplete = False
                    break
