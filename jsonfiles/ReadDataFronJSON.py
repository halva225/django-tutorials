import json

# read file
myjsonfile = open('jsonfiles\employee.json','r')
jsondata = myjsonfile.read()

# parse
obj = json.loads(jsondata)

print(str(obj['firstName']))
print(str(obj['lastName']))

list = obj['adress']
print(list)
print(len(list))

for i in range(len(list)):
    print("Adress of ",i,"is ...")
    print("Street:", list[i].get("street")),
    print("City:", list[i].get("city")),
    print("State:", list[i].get("state")),
