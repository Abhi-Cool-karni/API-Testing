import json

import requests

# get book by author name from GET method
response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName': 'Abhis K'},)
# print(response.text)
# print(type(response.text))
# string_response = response.text
# dict_response = json.loads(string_response)
# print(type(dict_response))
# print(dict_response[0]['isbn'])
# assert dict_response[0]['isbn'] == "bcd"

# second method
json_response = response.json()
print(type(json_response))
print(json_response[0]['isbn'])
assert json_response[0]['isbn'] == 'bcd'
