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

student = Student()


student.study()

print(student.grade)

student.study()

print(student.grade)

student.study()

print(student.grade)

student.study()

print(student.grade)

student.study()

print(student.grade)

student.study()

print(student.grade)

student.study()

print(student.grade)

student.study()

print(student.grade)

student.study()

print(student.grade)

student.study()

print(student.grade)

student.study()

print(student.grade)

student.study()

print(student.grade)

teacher = Teacher()

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



