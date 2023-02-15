class Student:

    def __init__(self, name, surname, gender) -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_courses(self, course):
        if course not in self.finished_courses:
            self.finished_courses.append(course)
        else:
            print('Ошибка')

    def add_courses_in_progress(self, course):
        if course not in self.courses_in_progress and course not in self.finished_courses:
            self.courses_in_progress.append(course)
        else:
            print('Ошибка')

    def rate_the_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')

    def __average_rating(self):
        result = []
        
        for i in self.grades.values():
            result.extend(i)

        return round(sum(result) / len(result), 2)

    def __str__(self) -> str:
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__average_rating()}\n' + \
        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

        return result

    def __lt__(self, student):
        if not isinstance(student, Student):
            print('Not a Student!')
            return
        return self.__average_rating() < student.__average_rating()

    def __gt__(self, student):
        if not isinstance(student, Student):
            print('Not a Student!')
            return
        return self.__average_rating() > student.__average_rating()


class Mentor:

    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_courses_attached(self, course):
        if course not in self.courses_attached:
            self.courses_attached.append(course)
        else:
            print('Ошибка')

    def __str__(self) -> str:
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result

class Lecturer(Mentor):

    def __init__(self, name, surname) -> None:
        super().__init__(name, surname)
        self.grades = {}

    def __average_rating(self):
        result = []
        
        for i in self.grades.values():
            result.extend(i)

        return round(sum(result) / len(result), 2)
    
    def __str__(self) -> str:
        return super().__str__() + f'\nСредняя оценка за лекции: {self.__average_rating()}'

    def __lt__(self, lectorer):
        if not isinstance(lectorer, Lecturer):
            print('Not a Lecturer!')
            return
        return self.__average_rating() < lectorer.__average_rating()

    def __gt__(self, lectorer):
        if not isinstance(lectorer, Lecturer):
            print('Not a Lecturer!')
            return
        return self.__average_rating() > lectorer.__average_rating()


class Reviewer(Mentor):

    def __init__(self, name, surname) -> None:
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


lecturer1 = Lecturer('Дмитрий', 'Васин')
lecturer2 = Lecturer('Галина', 'Крапивина')
lecturer3 = Lecturer('Марк', 'Тойотов')
lecturer4 = Lecturer('Бумер', 'Немецкий')
reviewer1 = Reviewer('Валерий', 'Тюрин')
reviewer2 = Reviewer('Анастасия', 'Ломоносова')
student1 = Student('Вася', 'Пупкин', 'мужской')
student2 = Student('Маша', 'Вашина', 'женский')
student3 = Student('Полина', 'Гагаринна', 'женский')
student4 = Student('Ринат', 'Галеев', 'мужской')


lecturer1.add_courses_attached('Fullstack Python')
lecturer1.add_courses_attached('Java')

lecturer2.add_courses_attached('Дизайн')
lecturer2.add_courses_attached('Системный аналитик')

lecturer3.add_courses_attached('Fullstack Python')

lecturer4.add_courses_attached('Fullstack Python')

reviewer1.add_courses_attached('Fullstack Python')
reviewer1.add_courses_attached('Системный аналитик')

reviewer2.add_courses_attached('Дизайн')
reviewer2.add_courses_attached('Java')

student1.add_finished_courses('Системный аналитик')
student1.add_courses_in_progress('Fullstack Python')
student1.rate_the_lecture(lecturer1, 'Fullstack Python', 7)
student1.rate_the_lecture(lecturer1, 'Fullstack Python', 8)
student1.rate_the_lecture(lecturer1, 'Fullstack Python', 9)
student1.rate_the_lecture(lecturer2, 'Системный аналитик', 9)
student1.rate_the_lecture(lecturer2, 'Системный аналитик', 8)
student1.rate_the_lecture(lecturer2, 'Системный аналитик', 8)

student2.add_finished_courses('Дизайн')
student2.add_courses_in_progress('Java')
student2.rate_the_lecture(lecturer1, 'Java', 6)
student2.rate_the_lecture(lecturer1, 'Java', 10)
student2.rate_the_lecture(lecturer1, 'Java', 3)
student2.rate_the_lecture(lecturer1, 'Java', 8)
student2.rate_the_lecture(lecturer2, 'Дизайн', 5)
student2.rate_the_lecture(lecturer2, 'Дизайн', 6)

student3.add_courses_in_progress('Fullstack Python')
student3.rate_the_lecture(lecturer3, 'Fullstack Python', 9)
student3.rate_the_lecture(lecturer3, 'Fullstack Python', 10)
student3.rate_the_lecture(lecturer4, 'Fullstack Python', 10)
student3.rate_the_lecture(lecturer4, 'Fullstack Python', 9)

student4.add_courses_in_progress('Fullstack Python')
student4.rate_the_lecture(lecturer3, 'Fullstack Python', 7)
student4.rate_the_lecture(lecturer3, 'Fullstack Python', 9)
student4.rate_the_lecture(lecturer4, 'Fullstack Python', 8)
student4.rate_the_lecture(lecturer4, 'Fullstack Python', 8)
student4.rate_the_lecture(lecturer4, 'Fullstack Python', 10)

reviewer1.rate_hw(student1, 'Системный аналитик', 5)
reviewer1.rate_hw(student1, 'Системный аналитик', 2)
reviewer1.rate_hw(student1, 'Системный аналитик', 7)
reviewer1.rate_hw(student1, 'Системный аналитик', 7)

reviewer1.rate_hw(student1, 'Fullstack Python', 5)
reviewer1.rate_hw(student1, 'Fullstack Python', 10)
reviewer1.rate_hw(student1, 'Fullstack Python', 9)
reviewer1.rate_hw(student1, 'Fullstack Python', 6)
reviewer1.rate_hw(student1, 'Fullstack Python', 4)

reviewer1.rate_hw(student3, 'Fullstack Python', 7)
reviewer1.rate_hw(student3, 'Fullstack Python', 7)
reviewer1.rate_hw(student3, 'Fullstack Python', 8)

reviewer1.rate_hw(student4, 'Fullstack Python', 9)
reviewer1.rate_hw(student4, 'Fullstack Python', 8)
reviewer1.rate_hw(student4, 'Fullstack Python', 9)
reviewer1.rate_hw(student4, 'Fullstack Python', 7)
reviewer1.rate_hw(student4, 'Fullstack Python', 10)

reviewer2.rate_hw(student2, 'Дизайн', 6)
reviewer2.rate_hw(student2, 'Дизайн', 10)

reviewer2.rate_hw(student2, 'Java', 10)
reviewer2.rate_hw(student2, 'Java', 10)
reviewer2.rate_hw(student2, 'Java', 7)
reviewer2.rate_hw(student2, 'Java', 7)
reviewer2.rate_hw(student2, 'Java', 9)
reviewer2.rate_hw(student2, 'Java', 5)
reviewer2.rate_hw(student2, 'Java', 10)

print(student1)
print(student2)
print(student3)
print(student4)
print(lecturer1)
print(lecturer2)
print(lecturer3)
print(lecturer4)
print(reviewer1)
print(reviewer2)

print(student1 > student2)
print(student4 > student3)
print(student3 < student2)
print(student3 > student2)

print(lecturer1 > lecturer2)
print(lecturer4 > lecturer3)
print(lecturer3 < lecturer2)
print(lecturer3 > lecturer2)

def awerage_rate_student(list_student, course):
    list_student_course = list(filter(lambda x: course in x.grades, list_student))
    
    list_grades = []
    for student in list_student_course:
        list_grades.extend(student.grades[course])
    
    return f'Средняя оценка по домашним заданиям среди студентов курса {course} равна {round(sum(list_grades) / len(list_grades), 2)}'

students = [student1, student2, student3, student4]
print(awerage_rate_student(students, 'Fullstack Python'))

def awerage_rate_lectors(list_lectors, course):
    list_lectors_course = list(filter(lambda x: course in x.grades, list_lectors))
    
    list_grades = []
    for lector in list_lectors_course:
        list_grades.extend(lector.grades[course])
    
    return f'Средняя оценка по лекциям среди лекторов курса {course} равна {round(sum(list_grades) / len(list_grades), 2)}'

lectors = [lecturer1, lecturer2, lecturer3, lecturer4]

print(awerage_rate_lectors(lectors, 'Fullstack Python'))