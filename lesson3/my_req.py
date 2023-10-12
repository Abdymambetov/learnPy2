import requests

my_response = requests.get('https://pypi.org/project/requests/')
# print(my_response)
# print(type(my_response))
# print(dir(my_response))
# print(my_response.text)
print(my_response.url)
print(my_response.status_code)