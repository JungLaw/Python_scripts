'''
(1) 

TASK: 
- json stored in working directory as 'snakes.json'. 
- load to python environment: 

'''

import json

# context manager: open a connection to the file and use the function json.load to load the JSON.
with open('snakes.json', r) as json_file:    json_data = json.load(json_file)

# file type
type(json_data)   

# print items
for key, value in json_data.items():
    print(key + ':", value)

                                               
'''
(2) 


"""


# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

