import time

seconds = int(input('How many seconds to wait? '))

for i in range(seconds):
    print(seconds - i)
    time.sleep(1)
print('times up!')
    
