from PersonDriver import Person
from PersonDriver import Teacher
from PersonDriver import Student

x = Person()
x.SetAddress('Promenade')
x.SetName('Emily')
print(x.__str__()+ '\n')

y = Teacher()
y.SetAddress('Outskirts')
y.SetName('Valen')
y.SetCourses(['Economics', 'Physics', 'Math', 'Biology'])
y.RemoveCourse('Physics')
print(y.__str__() + '\n')

z = Student()
z.SetAddress('Capitol')
z.SetName('Gunther')
z.SetGrades([85, 87, 90, 100])
z.SetCourses(['Classical Arts', 'Musical Theory', 'Graphic Design'])
z.SetNumCourses(4)
z.AddCourseGrade('Classical Arts', 85)
print(z.__str__())