#the json.load : used to read json document from file 
#the json.loads : used to convert the json string document in to the python dictionary.
#the json.dumps : return javascript object
import json

s = '{"kalu":"don"}'
print(s)

data = json.loads(s)
print(data['kalu'])