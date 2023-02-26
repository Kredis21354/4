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
    human.grade = 12

student = Student()
student2 = Student()
teacher = Teacher()

print('оцінка першого студента до',student.grade)
teacher.give_grade(student)
print('оцінка першого студента після',student.grade)

print('оцінка другогостудента до',student2.grade)
teacher.give_grade(student2)
print('оцінка другогостудента після',student2.grade)



