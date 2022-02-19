from random import choice

num = int(input('\nEnter the number of passwords: '))
while num <= 0:
    print('\n| Enter a number greater than 0 |\n')
    num = int(input('Enter the number of passwords: '))

length = int(input('Enter the length of passwords: '))
while length < 8 or length > 127:
    print('\n| The minimum password length is 8 characters'
          ' and the maximum is 127 |\n')
    length = int(input('Enter the length of passwords: '))

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
all_passwords = set()
while len(all_passwords) < num:
    password = ''
    for i in range(length):
        password += choice(chars)
    all_passwords.add(password)
all_passwords = list(all_passwords)

with open('passwords.txt', 'w') as output:
    for i in range(len(all_passwords)):
        output.write(f'{i+1}) {all_passwords[i]}' + '\n')

with open('passwords.txt') as output:
    print('\n' + output.read())
