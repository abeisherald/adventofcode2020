with open("day2input.txt") as input_list:
    password_list = input_list.read().splitlines()


valid_passwords = 0

for potential_password in password_list:
    password_policy = potential_password[:(potential_password.find(':'))]
    password = potential_password[(potential_password.find(':')+2):]
    password_policy_position1 = int(password_policy[:(
        password_policy.find('-'))])
    password_policy_position2 = int(password_policy[(
        password_policy.find('-')+1):password_policy.find(' ')])
    password_policy_letter = password_policy[(
        potential_password.find(' ')+1):]

    if (password[(password_policy_position1-1)] == password_policy_letter) is not (password[(password_policy_position2-1)] == password_policy_letter):
        valid_passwords += 1

print(valid_passwords)
