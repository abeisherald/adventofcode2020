with open("day2input.txt") as input_list:
    password_list = input_list.read().splitlines()


valid_passwords = 0

for potential_password in password_list:
    password_policy = potential_password[:(potential_password.find(':'))]
    password = potential_password[(potential_password.find(':')+1):]
    password_policy_amount = password_policy[:(
        potential_password.find(' '))]
    password_policy_letter = password_policy[(
        potential_password.find(' ')):].strip()

    if int(password_policy_amount[:(password_policy_amount.find('-'))]) <= password.count(password_policy_letter) <= int(password_policy_amount[(password_policy_amount.find('-')+1):]):
        valid_passwords += 1
print(valid_passwords)
