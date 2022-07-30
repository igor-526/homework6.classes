class Student:
    def __init__(self, name, surname,):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.grades = {}

    def rate_mentor(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in self.courses_in_progress and course in mentor.courses_attached:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            print('Ошибка')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')


def mean_grade(first, second):
    first_grades = []
    second_grades = []
    if type(first) == type(second):
        for discipline in first.grades:
            for grade in first.grades[discipline]:
                first_grades.append(grade)
        for discipline in second.grades:
            for grade in second.grades[discipline]:
                second_grades.append(grade)
    if sum(first_grades)/len(first_grades) > sum(second_grades)/len(second_grades):
        difference = sum(first_grades)/len(first_grades) - sum(second_grades)/len(second_grades)
    else:
        difference = sum(second_grades)/len(second_grades) - sum(first_grades)/len(first_grades)
    print(f'Средняя оценка {first.name} {first.surname} составляет {sum(first_grades)/len(first_grades)}.\nСредняя оценка {second.name} {second.surname} составляет {sum(second_grades)/len(second_grades)}.\nРазница: {difference}')


if __name__ == '__main__':
    k_grigoreva = Student('Карина', 'Григорьева')
    k_grigoreva.courses_in_progress += ['Python']
    k_grigoreva.courses_in_progress += ['Java']
    k_grigoreva.courses_in_progress += ['HTML']
    a_araslanova = Student('Алина', 'Арасланова')
    a_araslanova.courses_in_progress += ['Java']
    a_araslanova.courses_in_progress += ['HTML']
    a_araslanova.courses_in_progress += ['C++']
    i_mushka = Student('Илья', 'Мушка')
    i_mushka.courses_in_progress += ['Java']
    i_mushka.courses_in_progress += ['Python']
    i_mushka.courses_in_progress += ['C++']
    m_alekseeva = Lecturer('Мария', 'Алексеева')
    m_alekseeva.courses_attached += ['Python']
    m_alekseeva.courses_attached += ['Java']
    y_tsirkuynov = Lecturer('Юрий', 'Циркунов')
    y_tsirkuynov.courses_attached += ['Java']
    y_tsirkuynov.courses_attached += ['HTML']
    n_abramov = Reviewer('Никита', 'Абрамов')
    n_abramov.courses_attached += ['C++']
    n_abramov.courses_attached += ['Python']
    i_ivanov = Reviewer('Иван', 'Иванов')
    i_ivanov.courses_attached += ['HTML']
    i_ivanov.courses_attached += ['C++']
    k_grigoreva.rate_mentor(m_alekseeva, 'Python', 10)
    k_grigoreva.rate_mentor(y_tsirkuynov, 'Java', 3)
    k_grigoreva.rate_mentor(y_tsirkuynov, 'HTML', 6)
    a_araslanova.rate_mentor(m_alekseeva, 'Java', 7)
    a_araslanova.rate_mentor(y_tsirkuynov, 'HTML', 1)
    a_araslanova.rate_mentor(y_tsirkuynov, 'Java', 9)
    i_mushka.rate_mentor(m_alekseeva, 'Java', 6)
    i_mushka.rate_mentor(y_tsirkuynov, 'Java', 6)
    i_mushka.rate_mentor(m_alekseeva, 'Python', 10)
    n_abramov.rate_student(a_araslanova, 'C++', 9)
    n_abramov.rate_student(i_mushka, 'C++', 7)
    n_abramov.rate_student(k_grigoreva, 'Python', 8)
    n_abramov.rate_student(i_mushka, 'Python', 8)
    i_ivanov.rate_student(k_grigoreva, 'HTML', 3)
    i_ivanov.rate_student(a_araslanova, 'HTML', 1)
    i_ivanov.rate_student(a_araslanova, 'C++', 3)
    i_ivanov.rate_student(i_mushka, 'C++', 1)
