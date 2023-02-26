class Person:
  name = "Name"

  def __init__(self, name):
    self.name = name

class Student(Person):
  grade = 0
  def study(self):
    self.grade += 1
  
  def __init__(self):
    super().__init__("Student")
  
class Teacher(Person):
  salary = 0
  student = []

  def teach(self):
    self.salary += 500
  
  def __init__(self):
    super().__init__("Teacher")

  def give_grade(self, human):
    human.grade += 1

student = Student()




teacher = Teacher()

teacher.give_grade(student)

print(student.grade)

teacher.give_grade(student)

print(student.grade)

teacher.give_grade(student)

print(student.grade)

teacher.give_grade(student)

print(student.grade)

teacher.give_grade(student)

print(student.grade)

teacher.give_grade(student)

print(student.grade)

teacher.give_grade(student)

print(student.grade)

teacher.give_grade(student)

print(student.grade)

teacher.give_grade(student)

print(student.grade)

teacher.give_grade(student)

print(student.grade)

teacher.give_grade(student)

print(student.grade)

teacher.give_grade(student)

print(student.grade)










teacher.teach()

print(teacher.salary)

teacher.teach()

print(teacher.salary)

teacher.teach()

print(teacher.salary)

teacher.teach()

print(teacher.salary)

teacher.teach()

print(teacher.salary)

teacher.teach()

print(teacher.salary)

teacher.teach()

print(teacher.salary)

teacher.teach()

print(teacher.salary)

teacher.teach()

print(teacher.salary)

teacher.teach()

print(teacher.salary)

teacher.teach()

print(teacher.salary)

teacher.teach()

print(teacher.salary)

teacher.teach()

print(teacher.salary)



