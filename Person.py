class Person:
    def __init__(self, name = '', address = ''):
        self.__name = name
        self.__address = address

    def SetName(self, name):
        self.__name = name
    
    def SetAddress(self, address):
        self.__address = address

    def GetName(self):
        return self.__name
    
    def GetAddress(self):
        return self.__address
    
    def __str__(self):
        return f'{self.GetName()}({self.GetAddress()})'

class Teacher(Person):
    def __init__(self, name = '', address = '', NumCourses = 0, Courses = None):
        super().__init__(name, address)
        self.SetCourses(Courses)
        self.__NumCourses = NumCourses
    
    def SetNumCourses(self, NumCourses):
        self.__NumCourses = NumCourses

    def SetCourses(self, Courses):
        if Courses is None:
            self.__Courses = []
        else:
            self.__Courses = Courses

    def AddCourse(self, course = ''):  
        for i in self.__Courses:
            if course == i:
                return None
            else:
                return self.__Courses.append(course)
            
    def RemoveCourse(self, course = ''):
        for i in self.__Courses:
            if course == i:
                return self.__Courses.remove(course)
            else:
                return None
    
    def GetCourses(self):
        self.__Courses = ",".join(self.__Courses)
        return self.__Courses

    def GetNumCourses(self):
        return self.__NumCourses   
    
    def __str__(self):
        return f'Teacher: {self.GetName()}({self.GetAddress()})\nAny Added Courses ?: {self.AddCourse()}\nAny Removed Courses?: {self.RemoveCourse()}\nCourses: {self.GetCourses()}'

class Student(Person):
    def __init__(self, name = '', address = '', NumCourses = 0, Courses = None, grades = None):
        super().__init__(name, address)
        self.SetCourses(Courses)
        self.__NumCourses = NumCourses
        self.__grades = grades
    
    def SetNumCourses(self, NumCourses):
        self.__NumCourses = NumCourses
    
    def SetGrades(self, grades):
        if grades is None:
            self.__grades = []
        else:
            self.__grades = grades

    def SetCourses(self, Courses):
        if Courses is None:
            self.__Courses = []
        else:
            self.__Courses = Courses

    def AddCourseGrade(self, course = '', grade = int):
        if all(course == i for i in self.__Courses) == False:
            return False
        else:
            return self.__Courses.append(course), self.__grades.append(grade)
    
    def PrintGrades(self):
        return self.__grades
    
    def GetAverageGrade(self):
        return sum(self.__grades)/self.__NumCourses
    
    def GetCourses(self):
        self.__Courses = ",".join(self.__Courses)
        return self.__Courses
    
    def GetNumCourses(self):
        return self.__NumCourses 
    
    def __str__(self):
        return f'Student: {self.GetName()}({self.GetAddress()}\nCourses: {self.GetCourses()}\nGrades: {self.PrintGrades()}\nGet Average Grade: {self.GetAverageGrade()}'
    

    

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

