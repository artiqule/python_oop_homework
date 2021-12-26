class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def __str__(self):
        grades = []
        for grade in self.grades.values():
            grades += grade
        average_grade = sum(grades)/len(grades)
        res = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {average_grade}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Не является лектором")
            return
        grades_self = []
        grades_other = []
        for grade in self.grades.values():
            grades_self += grade
        aver_grade_self = sum(grades_self) / len(grades_self)
        for grade in other.grades.values():
            grades_other += grade
        aver_grade_other = sum(grades_other) / len(grades_other)
        return aver_grade_self < aver_grade_other

class Rewiewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname}"
        return res

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lec(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades = []
        for grade in self.grades.values():
            grades += grade
        average_grade = sum(grades)/len(grades)
        res = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {','.join(self.finished_courses)}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Не является студентом")
            return
        grades_self = []
        grades_other =[]
        for grade in self.grades.values():
            grades_self += grade
        aver_grade_self = sum(grades_self) / len(grades_self)
        for grade in other.grades.values():
            grades_other += grade
        aver_grade_other = sum(grades_other) / len(grades_other)
        return aver_grade_self < aver_grade_other


some_student = Student('Ruoy', 'Eman', 'gender')
some_student_2 = Student('Mary', 'Swan', 'gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['GIT']
some_student_2.courses_in_progress += ['GIT']

some_rewiewer = Rewiewer('Some', 'Buddy')
some_student.finished_courses += ['Введение в программирование']

some_lecturer = Lecturer("Oleg", "Bulygin")
some_lecturer_2 = Lecturer("Aleksandr", "Bardin")
some_lecturer.courses_attached += ['Python']
some_lecturer_2.courses_attached += ['GIT']
some_student.rate_lec(some_lecturer, 'Python', 10)
some_student.rate_lec(some_lecturer, 'GIT', 10)
some_student.rate_lec(some_lecturer_2, 'GIT', 10)
some_student.rate_lec(some_lecturer_2, 'Python', 9.8)
some_rewiewer.courses_attached += ['Python']
some_rewiewer.courses_attached += ['GIT']
some_rewiewer.rate_hw(some_student, 'Python', 10)
some_rewiewer.rate_hw(some_student, 'GIT', 9.8)
some_rewiewer.rate_hw(some_student_2, 'GIT', 10)

def calc_aver_grade (students, course):
    grades = []
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                grades += student.grades[course]
    aver_grade = sum(grades) / len(grades)
    return aver_grade
print(calc_aver_grade ([some_student, some_student_2], "Python"))

def calc_aver_grade_2 (lectors, course):
    grades_2 = []
    for lector in lectors:
        if isinstance(lector, Lecturer):
            if course in lector.grades:
                grades_2 += lector.grades[course]
    aver_grade = sum(grades_2) / len(grades_2)
    return aver_grade

print(calc_aver_grade_2 ([some_lecturer, some_lecturer_2], "Python"))



# print(some_lecturer.courses_attached)
# print(some_lecturer.grades)
# print(some_lecturer_2.grades)
# print(some_lecturer > some_lecturer_2 )
# print(some_reviewer)
# print(some_lecturer)
# print(some_student)
# print(some_student.grades)
# print(some_student_2.grades)
# print(some_student < some_student_2)