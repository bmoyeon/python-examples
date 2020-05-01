import random
import time

print('============================')
print('        Up/Down Game        ')
print('press any key to continue...')
print('============================')

input()

start = time.time()
count = 0

num = random.randint(1, 100)
while True:
    getnum = int(input('Please enter a number: '))
    count += 1

    if getnum > num:
        print('down')
    elif getnum < num:
        print('up')
    elif getnum == num:
        end = time.time()
        elapsed_time = int(end - start)
        print('correct!\n시도 횟수 : {0}\n총 걸린 시간 : {1} seconds.'.format(count, elapsed_time))
        break
