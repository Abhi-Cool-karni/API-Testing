import json

course = '{"name":"Abhishek", "languages":["JavaScript","Python"]}'

# Loads method parse json string and it returns dictionary

dict_course = json.loads(course)
print(type(dict_course))
print(dict_course)
print(dict_course['name'])
