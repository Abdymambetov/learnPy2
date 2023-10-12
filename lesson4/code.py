from random import randint
from datetime import datetime
#загадываем числло



#угадываем число, перебор / brute force
# for i in range(1,100):
#     if num == i:
#         print(f'Int: {i}')


n = 100

num = randint(1,n)
print(num)

prev_min = 1
prev_max = n

start = datetime.now()
k = 0
i = (prev_min + prev_max)//2

while True:
    k +=1
    print(i)
    if i == num:
        print(f'correct {i}' )
        break
    elif i > num:
        prev_max = i
        i = (prev_min + prev_max) //2
    elif i < num:
        prev_min = i
        i = (prev_min + prev_max) //2

print(f'Шагов: {k}')
end = datetime.now()
print(end - start)