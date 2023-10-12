from datetime import datetime


n = 1000
is_break = False
for a in range(1, n):
    for b in range(1,n):
        for c in range(1,n):
            if a **2 + b**2 == c**2 and a+b+c == 12 and a<b<c:
                print(a, b,c)


for a in range(1, n):
    for b in range(1, n):
        c = (a**2 + b**2) ** 0.5
        if a+b+c==n and a<b<c:
            print(a,b,c)
            print(a * b * c)
            is_break = True
            break
    if is_break:
        break



# hw
summ = 0

for i in range(1,1000):
    if i %3 == 0 or i%5 == 0:
        summ += i

print(summ)


##
prime_numbers = []
for i in range(2,1001):
    prime = True
    for divider in range(2, int(i ** 0.5) + 1):
        if i %divider == 0:
            prime = False
            break
    if prime:
        prime_numbers.append(i)
print(prime_numbers)

## решето_аткина

def resheto_atkina(limit):
    is_prime = dict()
    for x in range(1, limit+1):
        for y in range(1, limit+1):
            n = 4 * x**2 + y**2
            if n <= limit and (n %12 ==1 or n % 12 == 5):
                is_prime[n] = not is_prime.get(n, False)
            n = 3 * x**2 + y**2
            if n <= limit and n %12 == 7:
                is_prime[n] = not is_prime.get(n, False)
            n = 3 * x**2 - y**2
            if x>y and n<=limit and n %12 == 11:
                is_prime[n] = not is_prime.get(n, False)
    for x in range(5, int(limit **0.5) +1):
        if is_prime.get(x):
            for y in range(x**2, limit +1, x**2):
                is_prime[y] = False
    is_prime[2] = is_prime[3] = True
    prime_nums = [i for i, item in is_prime.items() if item]
    return prime_nums

nums_prime = resheto_atkina(10000)
print(nums_prime, 'lox')


##
class MyNumber():
    def __init__(self, power):
        self.value = 2**power

    def count_digits_sum(self):
        self.digits_sum = sum(int(digit) for digit in str(self.value))
        return self.digits_sum
    
num_1 = MyNumber(15) # 15 - это степень
print(num_1.value) # 32768
print(num_1.count_digits_sum()) # 26

num_2 = MyNumber(1000) # 1000 - это степень
print(num_2.value) # Большое число (скрыто для краткости)
print(num_2.count_digits_sum()) # Сумма цифр этого числа


