import copy


with open('day4input.txt') as passport_batch:
    passport_list = passport_batch.read().splitlines()

fields_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
fields_satisfied = {'byr': False, 'iyr': False, 'eyr': False,
                    'hgt': False, 'hcl': False, 'ecl': False, 'pid': False, 'cid': False}


for passport_line in passport_list:
    if passport_line == ' ':
        determine_eligibility

    else:
        temp = copy.copy(passport_line)
        while temp != '':
            field = temp[:(temp.find(' '))]
            field_type = field[:field.find(':')]
            fields_satisfied[field_type] = True

            try:
                temp = temp[(temp.find(' ')+1):]
            except:
                break
