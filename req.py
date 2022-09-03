import requests as requests

url = 'https://jsonplaceholder.typicode.com/todos/2'

response = requests\
    .get(url)

# print(type(response))
# print(response)
# print(response.status_code)
# print(response.text)
# print(response.text[0])
# print(type(response.json()))
print(response.json()['userId'])
print(response.json()['id'])
print(response.json()['title'])
print(response.json()['completed'])
