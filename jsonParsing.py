import json


def find_emp_by_year(jsonFile):
    with open(jsonFile, 'r') as file:
        jsonData = json.load(file)
    data = find_emp(jsonData['data'])
    # txt file
    target_file = 'empreport.txt'
    matched_emp_file(data, target_file)


def find_emp(employees):
    matchednames=[]
    for emp in employees:
        name = emp["name"]
        if emp['year'] > 2002:
            matchednames.append(name)
    print(matchednames)
    return matchednames


def matched_emp_file(data, target_file):
    with open(target_file, 'w') as file:
        for emp in data:
            file.writelines(str(emp) + '\n')


if __name__ == '__main__':
    find_emp_by_year('emp.json')
