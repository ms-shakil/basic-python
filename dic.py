import json

JSON_FILE = "./dic_enginner.json"

list_of_engineers = []

with open(JSON_FILE, 'r') as data_file:
    list_of_dicts = json.load(data_file)
    list_of_engineers = list_of_dicts
    # for d in list_of_dicts:
    #     list_of_engineers.append(d)

print("There are {} engineers in the file".format(len(list_of_engineers)))

count = int(input("Enter number of engineers: "))

def find_engineer(list, id):
    found = False
    for data in list:
        if data["id"] == id:
            found = True
            break
    return found

i = 0
while i < count:
    # print("# Enter data for engineer #{}".format(i+1))
    engineer = {
        "id": input('ID: '),
        "name": input("Name: "),
        "age": input("Age: "),
        "district": input("District: ")
    }
    if find_engineer(list_of_engineers, engineer['id']) == True:
        print("This engineer already exists")
    else:
        list_of_engineers.append(engineer)
        i += 1

with open(JSON_FILE, "w") as data_file:
    json.dump(list_of_engineers, data_file)


