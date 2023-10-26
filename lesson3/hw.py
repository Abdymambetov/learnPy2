from bestlib import Balance, make_report
import requests

my_balance = Balance(1234)
print(my_balance.money)

res_1 = requests.get('https://jsonplaceholder.typicode.com/posts/1')
res_2 = requests.get('https://habr.com/ru/companies/vk/articles/692062/')
res_3 = requests.get('https://habr.com/ru/primer')

make_report(res_1)
make_report(res_2)
make_report(res_3)

print(res_1.status_code, res_1.url)
print(res_2.status_code, res_2.url)
print(res_3.status_code, res_3.url)

# print(res_1.text)
# print(res_2.text)
