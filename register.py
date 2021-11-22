class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_sm(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in mentor.courses_attached and course in self.courses_in_progress:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self):
        list_score = []
        for subj, score in self.grades.items():
            list_score += score
        return round(sum(list_score)/len(list_score), 2)


    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {self.average()}\n'
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return self.average() < other.average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.average()}')
        return res

    def average(self):
        list_score = []
        for subj, score in self.grades.items():
            list_score += score
        return round(sum(list_score) / len(list_score), 2)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return self.average() < other.average()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_rs(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def average_mark_st(students, course):
    list_score = []
    for student in students:
        for k, v in student.grades.items():
            if course == k:
                list_score += v
    print(f'Средний балл за домашние задания по курсу {course}: {round(sum(list_score) / len(list_score), 2)}')

def average_mark_lect(mentors_lect, course):
    list_score = []
    for lecturer in mentors_lect:
        for k, v in lecturer.grades.items():
            if course == k:
                list_score += v
    print(f'Средний балл лекторов по курсу {course}: {round(sum(list_score) / len(list_score), 2)}')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Java', 'C++', 'Pascal', 'PHP']
best_student.finished_courses += ['Math', 'Literature']

worse_student = Student('Anna', 'Borina', 'female')
worse_student.courses_in_progress += ['Python', 'Java', 'C++', 'PHP']
worse_student.finished_courses += ['Введение в программирование']

students = [best_student, worse_student]

mentor_rev = Reviewer('Bill', 'Zeman')
mentor_rev.courses_attached += ['Python', 'Java', 'C++']

mentor_lect_doc = Lecturer('Some', 'Buddy')
mentor_lect_doc.courses_attached += ['Python', 'Java', 'C++']

mentor_lect_prof = Lecturer('Ivan', 'Petrov')
mentor_lect_prof.courses_attached += ['Python', 'Java', 'C++', 'PHP']

mentors_lect = [mentor_lect_prof, mentor_lect_doc]

best_student.rate_sm(mentor_lect_doc, "Python", 7)
best_student.rate_sm(mentor_lect_doc, "Python", 6)
worse_student.rate_sm(mentor_lect_doc, "Python", 8)
worse_student.rate_sm(mentor_lect_doc, "Java", 7)

best_student.rate_sm(mentor_lect_prof, "PHP", 8)
best_student.rate_sm(mentor_lect_prof, "PHP", 9)
worse_student.rate_sm(mentor_lect_prof, "C++", 8)
worse_student.rate_sm(mentor_lect_prof, "C++", 9)

mentor_rev.rate_rs(best_student, "Python", 6)
mentor_rev.rate_rs(best_student, "Python", 5)
mentor_rev.rate_rs(best_student, "Python", 4)

mentor_rev.rate_rs(best_student, "Java", 6)
mentor_rev.rate_rs(best_student, "C++", 5)
mentor_rev.rate_rs(best_student, "C++", 4)

mentor_rev.rate_rs(worse_student, "Python", 3)
mentor_rev.rate_rs(worse_student, "Python", 4)
mentor_rev.rate_rs(worse_student, "Python", 4)

mentor_rev.rate_rs(worse_student, "Java", 4)
mentor_rev.rate_rs(worse_student, "C++", 3)
mentor_rev.rate_rs(worse_student, "C++", 3)

print(best_student.grades)
print(best_student)
print()
print(worse_student.grades)
print(worse_student)
print()
print(mentor_lect_prof.grades)
print(f'Преподаватель лектор профессор:\n{mentor_lect_prof}')
print()
print(mentor_lect_doc.grades)
print(f'Преподаватель лектор доцент:\n{mentor_lect_doc}')
print()
print(f'Преподаватель проверяющий:\n{mentor_rev}')
print()
print(mentor_lect_doc < mentor_lect_prof)
print(best_student > worse_student)
print()
average_mark_st(students, 'Python')
average_mark_lect(mentors_lect, 'Python')
