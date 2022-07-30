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

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка! Вы сравниваете разные роли!')
        else:
            print(f'Средняя оценка студента {self.name} {self.surname}: {get_mean(self.grades)}')
            print(f'Средняя оценка студента {other.name} {other.surname}: {get_mean(other.grades)}')
            if get_mean(self.grades) > get_mean(other.grades):
                return f'Разница составляет: {get_mean(self.grades) - get_mean(other.grades)}'
            else:
                return f'Разница составляет: {get_mean(other.grades) - get_mean(self.grades)}'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {get_mean(self.grades)}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка! Вы сравниваете разные роли!')
        else:
            print(f'Средняя оценка лектора {self.name} {self.surname}: {get_mean(self.grades)}')
            print(f'Средняя оценка лектора {other.name} {other.surname}: {get_mean(other.grades)}')
            if get_mean(self.grades) > get_mean(other.grades):
                return f'Разница составляет: {get_mean(self.grades)-get_mean(other.grades)}'
            else:
                return f'Разница составляет: {get_mean(other.grades)-get_mean(self.grades)}'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Специализация: {", ".join(self.courses_attached)}\n' \
               f'Средняя оценка за лекции: {get_mean(self.grades)}'


class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Специализация: {", ".join(self.courses_attached)}'


def get_mean(grades_list):
    all_grades = []
    for discipline in grades_list:
        for grade in grades_list[discipline]:
            all_grades.append(grade)
    return sum(all_grades)/len(all_grades)


def get_mean_course(people_list, course):
    all_grades = []
    for people in people_list:
        if type(people) == type(people_list[0]):
            if course in people.grades:
                for grade in people.grades[course]:
                    all_grades.append(grade)
            else:
                print(f'Ошибка! {people.name} {people.surname} не имеет специализации {course}!')
        else:
            print('Ошибка! Вы смешали людей разных ролей!')
    return sum(all_grades) / len(all_grades)


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
