import json

JSON_FILE = "./dic_student.json"

data_dict = {
    "name": "Data of students",
    "total": 0,
    "districts": [],
    "students": []
}

with open(JSON_FILE, 'r') as json_file:
    try:
        data = json.load(json_file)
        data_dict['name'] = data['name']
        data_dict['total'] = data['total']
        data_dict['districts'] = data['districts']
        data_dict['students'] = data['students']
    except Exception:
        print('No data found in file')

print("There are {} students in the file".format(data_dict['total']))

count = int(input("Enter number on students: "))

def find_student(list, id):
    found = False
    for data in list:
        if data['id'] == id:
            found = True
            break
    return found

i = 0
while i < count:
    print("Enter data of student #{}".format(i+1))
    student = {
        "id": input("ID:"),
        "name": input("Name:"),
        "age": input("Age:"),
        "district": input("District:")
    }
    if find_student(data_dict['students'], student["id"]) == True:
        print("This student already exists:")
    else:
        data_dict['students'].append(student)
        i += 1

data_dict['total'] = len(data_dict['students'])
dist_counts = {}
dists_list = []

for student in data_dict['students']:
    dist = student['district']
    if dist in dist_counts:
        dist_counts[dist] += 1
    else:
        dist_counts[dist] = 1

for name, count in dist_counts.items():
    dists_list.append({
        "name": name,
        "count": count
    })

data_dict['districts'] = dists_list

with open(JSON_FILE, "w") as data:
    json.dump(data_dict, data)
