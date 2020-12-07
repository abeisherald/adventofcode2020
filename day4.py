

with open('day4input.txt') as passport_batch:
    passport_list = passport_batch.read().splitlines()

fields_satisfied = {'byr': False, 'iyr': False, 'eyr': False,
                    'hgt': False, 'hcl': False, 'ecl': False, 'pid': False}

# 'cid': False

eligible = 0

for passport_line in passport_list:
    if passport_line == '':
        if False not in fields_satisfied.values():
            eligible += 1
            #print(f'eligible, fields:{fields_satisfied}')
        else:
            print(f'ineligible, fields:{fields_satisfied}')
        fields_satisfied = {
            field: False for field in fields_satisfied if field != 'cid'}

    else:
        while passport_line != '':
            space_index = passport_line.find(' ')
            field = passport_line[:(
                space_index if space_index != -1 else len(passport_line))]
            field_type = field[:field.find(':')]
            fields_satisfied[field_type] = True

            passport_line = passport_line.replace(field, '').lstrip()

print(eligible)
