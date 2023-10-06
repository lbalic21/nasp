from xml.etree.ElementTree import tostring


class Person:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def increase_age(self) :
        self.age += 1

    def print(self) :
        print(self.name + ", " + str(self.age))

        
class PersonDetail(Person):
    def __init__(self, name, age, adress) :
        self.adress = adress
        Person.__init__(self, name, age)

    def print(self) :
        Person.print(self)
        print("Adresa: " + self.adress)

    


first_person = Person("Marko", 39)
second_person = Person("Ivan", 17)

first_person.print()
second_person.print()

second_person.increase_age()
second_person.print()

first_person_detail = PersonDetail("Ana", 25, "Unska 3")

first_person_detail.print()

first_person_detail.increase_age()
first_person_detail.print()

