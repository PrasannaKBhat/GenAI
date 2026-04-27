import json

data = {
    "name": "Pranav",
    "age": 25,
    "role": "Gen AI engineer"
}

with open("withoutindent.json" , "w") as file:
    json.dump(data,file)

print("Json file created successfully")    