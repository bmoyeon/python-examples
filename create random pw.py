import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

number = int(input('Number of passwords? '))
length = int(input('Password length? '))

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
