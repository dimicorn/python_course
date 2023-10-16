class Person(object):
    def __init__(self, name: str, age: int, nationality: str) -> None:
        self.name, self.age, self.nationality = name, age, nationality
    
    def how_long2live(self):
        life = 70
        self.how_long = life - self.age
        return self.how_long

class MIPT(object):
    UNIVERSITY = 'MIPT'
    def __init__(self, rating: int) -> None:
        self.rating = rating

class Student(Person):
    ...

class MIPTStudent(Student, MIPT):
    def __init__(self, name: str, age: int, 
                 nationality: str, sleep_hours_a_week: int) -> None:
        self.name, self.age, self.nationality, self.sleep_hours_a_week = (
        name, age, nationality, sleep_hours_a_week
        )
        self.UNIVERSITY = super().UNIVERSITY
    
    def parent_attribute(self):
        return self.UNIVERSITY
    
s = Person('Ivan', 20, 'Russian')
# print(s.how_long) # error
s.how_long2live()
print(s.how_long)
# print(s.name) # error

mipt_s = MIPTStudent('Dima', 20, 'Russian', 0)
print(mipt_s.UNIVERSITY)
print(mipt_s.parent_attribute())