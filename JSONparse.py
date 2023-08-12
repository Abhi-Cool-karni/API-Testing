import json

course = '{"name":"Abhishek", "languages":["JavaScript","Python"]}'

# Loads method parse json string and it returns dictionary

dict_course = json.loads(course)
print(type(dict_course))
print(dict_course)
print(dict_course['name'])
# get me the first language thought by trainer
# list_language = dict_course['languages']
# print(list_language)
# print(type(list_language))
# print(list_language[0])

# shorthand
print(dict_course['languages'][0])

# ******** Parse content present in JSON file

with open("C:\\Users\\Abhishek Kulkarni\\Desktop\\AK\\Software Testing\\course.json") as f:
    data = json.load(f)
    print(data)
    # print(type(data))
    # print(data['courses'])
    print(data['courses'][1]['title'])
    print(data['dashboard'])
    print(type(data['dashboard']))
    print(data['dashboard']['website'])
