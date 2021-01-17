from collections import namedtuple
Student = namedtuple("student_tuple", ["name", "age", "department"])

Alina = Student(name="Alina", age="22", department="linguistics")
Alex = Student("Alex", "25", "programming")
Kate = Student("Kate", "19", "art")

print(Alina, Alex, Kate, sep='\n')
