import json


functions = dict()
functions['function1'] = ['1', '2']
functions['function2'] = ['1', '2']

file = open('test_config.json', 'w+')
json.dump(functions, file)
file.close()