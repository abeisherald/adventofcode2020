
with open("day1input.txt") as input_list:
    x = input_list.read().splitlines()
    newx = [int(a) for a in x]

    # print(newx)

sum_x = 2020

for index, var_a in enumerate(newx):
    for var_b in newx[(index+1):]:
        if (var_a + var_b) == sum_x:
            print(
                f'variable a is:{var_a} and variable b is:{var_b}. Multiplied against each other results in:{var_a * var_b}')
        else:
            continue
