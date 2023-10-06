person_data = {
    "Ana" : 1995,
    "Zoran" : 1978, 
    "Lucija" : 2001, 
    "Anja" : 1997
}

print(person_data)

for person in person_data :
    person_data[person] -= 1
    
print(person_data)

year_age = []

for person in person_data :
    year = person_data[person]
    person_tuple = (year, 2022 - year)
    year_age.append(person_tuple)

print(year_age)