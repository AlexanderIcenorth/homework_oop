class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def _average_grade(self):
        grades_summ = 0
        grades_count = 0
        for grades_lists in self.grades.values():            
            for grades in grades_lists:
                grades_summ += grades
                grades_count += 1
        result = grades_summ / grades_count
        result = round(result, 2)
        return result

    def __str__(self):
        result1 = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grade()}\n'
        result2 = f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return result1 + result2

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Надо сравнивать студентов cо студентами!')
            return
        return self._average_grade() < other._average_grade()

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
   
class Reviewer(Mentor):        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result
 
class Lecturer(Mentor):
    grades = {}

    def _average_grade(self):
        grades_summ = 0
        grades_count = 0
        for grades_lists in self.grades.values():            
            for grades in grades_lists:
                grades_summ += grades
                grades_count += 1
        result = grades_summ / grades_count
        result = round(result, 2)
        return result

    def __str__(self):
        result  = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade()}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Надо сравнивать лекторов c лекторами!')
            return
        return self._average_grade() < other._average_grade()


stud1 = Student('Антонио', 'Мимокрокодилов', 'муж')
stud1.finished_courses = ['Прыжки в сторону', 'Гудение пчелой']
stud1.courses_in_progress = ['Хромоногие пляски', 'Метание шакалов']
stud1.grades = {'Хромоногие пляски': [6, 7, 9, 10, 8, 10],'Метание шакалов': [9, 6, 10, 1, 7, 8]}

stud2 = Student('Юлиана','Черездорогуногузадерищенко', 'жен')
stud2.finished_courses = ['Хромоногие пляски', 'Метание шакалов']
stud2.courses_in_progress = ['Прыжки в сторону', 'Гудение пчелой']
stud2.grades = {'Прыжки в сторону': [3, 5, 10, 6, 8, 9],'Гудение пчелой': [8, 10, 10, 9, 10, 9]}

stud3 = Student('Кирюха', 'Пупков', 'муж')
stud3.finished_courses = ['Гудение пчелой']
stud3.courses_in_progress = ['Хромоногие пляски', 'Метание шакалов', 'Прыжки в сторону']
stud3.grades = {'Хромоногие пляски' : [3, 2, 3, 4], 'Метание шакалов' : [1, 1, 1, 0], 'Прыжки в сторону' : [3, 5, 1, 2]}

lect1 = Lecturer('Сбегастий', 'Запахложаренков')
lect1.courses_attached = ['Прыжки в сторону', 'Хромоногие пляски']
lect1.grades = {'Прыжки в сторону': [9, 10, 10, 10, 9, 10], 'Хромоногие пляски': [8, 9, 10, 7, 10, 10]}

lect2 = Lecturer('Запопий', 'Внезапноукусов')
lect2.courses_attached = ['Гудение пчелой', 'Метание шакалов']
lect2.grades = {'Гудение пчелой' : [7,10, 6, 8, 9, 9], 'Метание шакалов':[10,10,10,10,10,10]}

rev1 = Reviewer('Анонимия', 'Инкогнитова')
rev1.courses_attached = ['Гудение пчелой', 'Хромоногие пляски']

rev2 = Reviewer('Вилен', 'Коммунаров')
rev2.courses_attached = ['Прыжки в сторону', 'Метание шакалов']

print(rev1)
print(lect2)
print(lect1 < lect2)
print(stud3)
print(stud1 < stud2)

students_list1 = [stud1, stud2, stud3]
students_list2 = []

def average_homevork_grade(list, course):
    '''
    Подсчёт средней оценки среди всех студентов, изучающих курс.
    '''
    all_studs_result = 0
    all_studs_count = 0
    for student in list:
        if course in student.grades.keys():
            grades_one_stud_summ = 0
            grades_one_stud_count = 0
            for course_name, grades_list in student.grades.items():
                if course_name == course:
                    for grade in grades_list:
                        grades_one_stud_summ += grade
                        grades_one_stud_count += 1
            result_one_stud = grades_one_stud_summ / grades_one_stud_count
            all_studs_count += 1
            all_studs_result = (all_studs_result + result_one_stud) / all_studs_count
    all_studs_result = round(all_studs_result, 2)
    if all_studs_result > 0:
        return all_studs_result
    else:
         return f'В этом списке студентов нет изучающих {course}'

print(average_homevork_grade(students_list1, 'Хромоногие пляски'))

def average_review_grade(list, course):
    '''
    Подсчёт средней оценки среди всех лекторов, преподающих курс.
    '''
