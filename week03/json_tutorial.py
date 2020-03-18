import json

my_object = {'name': 'Marto', 'age': 24, 'interests': ['sport', 'AI']}

with open('example.json', 'w') as f:
    # Saves my_object in the example.json file
    json.dump(my_object, f)

with open('example.json', 'r') as f:
    # Reads example.json file
    my_read_object = json.load(f)
    print(my_object)
    print(type(my_object))
