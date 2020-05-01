from random import randint
# randint(a, b): a와 b 사이의 랜덤한 정수 반환

repeat = True

while repeat:
    print('You rolled', randint(1, 6))
    print('Do you want to roll again? Y/N')
    repeat = ('y' or 'yes') in input().lower()
