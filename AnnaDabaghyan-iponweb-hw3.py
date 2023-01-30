# 13. sub_year
# 14. sub_month
# 15. sub_day
# 16. sub_hour
# 17. sub_minute
# 18. sub_second
# 19. __add__
# 20. __sub__

import calendar


class Date:
    def __init__(self, day, month, year):
        self.__year = year
        self.__month = month
        self.__day = day

    md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __repr__(self):
        return 'Date: {}.{}.{}'.format(self.__day, self.__month, self.__year)

    def __is_leap_year(self):
        if self.__year % 400 == 0:
            self.md[1] = 29
            return True
        elif self.__year % 100 == 0:
            self.md[1] = 28
            return False
        elif self.__year % 4 == 0:
            self.md[1] = 29
            return True
        else:
            self.md[1] = 28
            return False

    def __year_days(self):
        self.__is_leap_year()
        return sum(self.md)

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @day.setter
    def day(self, other):
        self.__day = other

    @month.setter
    def month(self, other):
        self.__month = other

    @year.setter
    def year(self, other):
        self.__year = other

    # will work only if x <= 31/30/28/29
    def __change_day_for_day_change(self, x):
        self.__is_leap_year()
        self.__day += x

    def __change_month_year_for_day_change(self, x):
        # while x + self.__day <= self.md[self.__month - 1] + self.md[self.__month]:
        self.__is_leap_year()
        self.__day = (x + self.__day) % self.md[self.__month - 1]
        self.__month += 1
        if self.__month > 12:
            self.__month = 1
            self.__year += 1

        # self.__year += x + sum(self.md[0:self.__month - 1]) + self.__day // self.__year_days()
        # bla = x + sum(self.md[0:self.__month - 1]) + self.__day % self.__year_days()
        # month_x = 0
        # for i in self.md:
        # while x + sum(self.md[0:self.__month - 1]) + self.__day <= self.__year_days():
        # while x + self.__day <= self.md[self.__month - 1] + self.md[self.__month]:

    def add_day(self, x):
        if self.__day + x <= self.md[self.__month - 1]:
            self.__change_day_for_day_change(x)
        else:
            self.__change_month_year_for_day_change(x)

    def add_month(self):
        self.__is_leap_year()
        if self.md[self.__month - 1] != self.md[self.__month] and self.__day == self.md[self.__month - 1]:
            if self.md[self.__month - 1] < self.md[self.__month]:
                self.__month += 1
            else:
                self.__month += 1
                self.__day = self.md[self.__month - 1]
        elif self.__month == 11:
            self.__year += 1
            self.__month = 1
        else:
            self.__month += 1

    def add_year(self, x):
        if self.__month == 2 and self.__day == 29 and calendar.isleap(self.__year + x) is False \
                and calendar.isleap(self.__year) is True:
            self.__year += x
            self.__month = 3
            self.__day = 1
        else:
            self.__year += x


# d = Date(31, 12, 2000)
# print(d.__repr__())
# d.add_day(30)
# print(d.__repr__())
# d.add_month()
# print(d.__repr__())
# d.add_year(10)
# print(d.__repr__())


class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __repr__(self):
        return 'Time: {}:{}:{}'.format(self.__hour, self.__minute, self.__second)

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, other):
        self.__hour = other

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, other):
        self.__minute = other

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, other):
        self.__second = other

    def add_seconds(self, x):
        if (self.__second + x) in range(1, 60):
            self.__second += x

        elif (self.__second + x) in range(60, 3600):
            self.__minute += (self.__second + x) // 60
            self.__second = (self.__second + x) % 60

        elif (self.__second + x) >= 3600:
            self.__minute = (self.__minute + ((self.__second + x) // 60)) % 60
            self.__hour = (self.__hour + (self.__second + x) % 3600) % 24
            self.__second = (self.__second + x) % 60
            # if self.hour >= 24:
            #     self.hour = self.hour % 24

    def add_minutes(self, x):
        if (self.__minute + x) in range(1, 60):
            self.__minute += x

        elif (self.__minute + x) >= 60:
            self.__hour += ((self.__minute + x) // 60) % 24
            self.__minute = (self.__minute + x) % 60

    def add_hour(self, x):
        self.__hour += x
        if self.__hour >= 24:
            self.__hour = self.__hour % 24

    def sum_of_times(x, y):
        # x = Time(x.hour, x.minute, x.second)
        # y = Time(0,0,0)
        a = y.__hour + x.__hour
        b = y.__minute + x.__minute
        c = y.__second + x.__second

        if c >= 60:
            b = (b + (c // 60)) % 60
            a = (a + (c // 3600)) % 24
            c = c % 60

        if b >= 60:
            a = (a + (b // 60)) % 24
            b = b % 60

        if a >= 24:
            a = a % 24

        return Time(a, b, c)


class DateTime:
    def __init__(self, date: Date, time: Time):
        self.__date = date
        self.__time = time

    def __repr__(self):
        print(self.__date.__repr__())
        print(self.__time.__repr__())

    @property
    def get_time(self):
        return self.__time

    @property
    def get_date(self):
        return self.__date

    def set_time(self, a, b, c):
        self.__time.hour = a
        self.__time.minute = b
        self.__date.second = c
        # return self.__time, self.__date

    def set_date(self, a, b, c):
        self.__date.year = a
        self.__date.month = b
        self.__date.day = c
        # return self.__time, self.__date


# dt = DateTime(Date(1,1,2000), Time(10,10,10))
# dt.__repr__()


class Company:
    def __init__(self, name, date, count):
        self.__company_name = name
        self.__founded_at = date
        self.__employees_count = count

    def __repr__(self):
        return "{}, founded at {}, {} people work there".format(self.__company_name, self.__founded_at,
                                                                self.__employees_count)

    @property
    def company_name(self):
        return self.__company_name

    @property
    def founded_at(self):
        return self.__founded_at

    @property
    def employees_count(self):
        return self.__employees_count

    @company_name.setter
    def company_name(self, other):
        self.__company_name = other

    @founded_at.setter
    def founded_at(self, other):
        self.__founded_at = other

    @employees_count.setter
    def employees_count(self, other):
        self.__employees_count = other


# aca = Company('ACA', 2015, 40)
# print(aca.employees_count)
# print(aca.company_name)
# print(aca.founded_at)
# print(aca.__repr__())


class Job:
    def __init__(self, company, salary, experience, position):
        self.__company_type = company
        self.__salary = salary
        self.__experience_year = experience
        self.__position = position

    def __repr__(self):
        return "Company name is: {}, expected salary is {}, you need to have {} years of experience," \
               " for the {}'s position".format(self.__company_type, self.__salary, self.__experience_year,
                                               self.__position)

    @property
    def company_type(self):
        return self.__company_type

    @property
    def salary(self):
        return self.__salary

    @property
    def experience_year(self):
        return self.__experience_year

    @property
    def position(self):
        return self.__position

    @company_type.setter
    def company_type(self, new_company):
        self.__company_type = new_company

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary

    @experience_year.setter
    def experience_year(self, new_experience):
        self.__experience_year += new_experience

    @position.setter
    def position(self, new_position):
        self.__position = new_position


class Person:
    def __init__(self, name, surname, gender, age, address, friends, job):
        self.__person_name = name
        self.__person_surname = surname
        self.__person_gender = gender
        self.__person_age = age
        self.__person_address = address
        self.__person_friends = friends
        self.__person_job = job

    def __repr__(self):
        return "Full name: {} {}, Gender: {}, Age: {}, Address: {},\nJobs: {} \nFriends: " \
               "{}".format(self.__person_name, self.__person_surname, self.__person_gender, self.__person_age,
                           self.__person_address, self.__person_job, self.__person_friends)

    @property
    def person_name(self):
        return self.__person_name

    @property
    def person_surname(self):
        return self.__person_surname

    @property
    def person_gender(self):
        return self.__person_gender

    @property
    def person_age(self):
        return self.__person_age

    @property
    def person_address(self):
        return self.__person_address

    @property
    def person_friends(self):
        return self.__person_friends

    @property
    def person_job(self):
        return self.__person_job

    @person_name.setter
    def person_name(self, other):
        self.__person_name = other

    @person_surname.setter
    def person_surname(self, other):
        self.__person_surname = other

    @person_gender.setter
    def person_gender(self, other):
        self.__person_gender = other

    @person_age.setter
    def person_age(self, other):
        self.__person_age = other

    @person_address.setter
    def person_address(self, other):
        self.__person_address = other

    def add_friend(self, new_friend):
        self.__person_friends.append(new_friend)
        new_friend.__person_friends += 1

    def remove_friend(self, ex_friend):
        self.__person_friends.remove(ex_friend)
        ex_friend.__person_friends -= 1

    def add_job(self, new_job):
        self.__person_job.append(new_job)
        self.__person_job.__company_type.__employees_count += 1

    def remove_job(self, ex_job):
        a = self.__person_job.remove(ex_job)
        self.__person_job.__company_type.__employees_count -= 1


# aca = Company('ACA', 2015, 40)
# job1 = Job(aca, 100, 3, 'Program Manager')
# job2 = Job(aca, 1111100, 4, 'CEO')
# person1 = Person('Anna', 'Dabaghyan', 'Female', 27, 'Abovyan', [], [job1])
# person2 = Person('Hakob', 'Hakobyan', 'Male', 30, 'Yerevan', [person1], [job2])
# # print(person1.person_friends)
# # person1.add_friend(person2)
# # print(person1.person_friends)
# # print(person1.person_job)
# person1.add_job(job2)
# print(person1.person_job)
# # print(person1.__repr__())


class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    def __repr__(self):
        return self.__amount, self.__currency

    @property
    def amount(self):
        return self.__amount

    @property
    def currency(self):
        return self.__currency

    @amount.setter
    def amount(self, new):
        self.__amount = new

    @currency.setter
    def currency(self, new):
        self.exchange_money(new)
        self.__currency = new

    exchange = {'AMD': 1, 'RUB': 5.8, 'USD': 400, 'EUR': 430}

    def exchange_money(self, new_cur):
        if self.__currency == list(self.exchange.keys())[0]:
            for i in list(self.exchange.keys())[1::]:
                if i == new_cur:
                    self.__currency = new_cur
                    self.__amount = round(self.__amount / self.exchange[i], 2)
        elif self.__currency in list(self.exchange.keys())[-1:0:-1]:
            if new_cur == list(self.exchange.keys())[0]:
                self.__amount = self.amount * self.exchange[self.__currency]
                self.__currency = new_cur
            elif new_cur in list(self.exchange.keys())[-1:0:-1] and new_cur != self.__currency:
                self.amount = round(self.amount * self.exchange[self.currency] / self.exchange[new_cur], 2)
                self.__currency = new_cur

    def __add__(self, other):
        if self.__currency == other.__currency:
            self.__amount += other.__amount
        else:
            self.exchange_money(other.__currency)
            self.__amount += other.__amount

    def __sub__(self, other):
        if self.__currency == other.__currency:
            self.__amount = abs(self.__amount - other.__amount)
        else:
            self.exchange_money(other.__currency)
            self.__amount = abs(self.__amount - other.__amount)

    def __truediv__(self, other):
        if self.__currency == other.__currency:
            self.__amount = self.__amount / other.__amount
        else:
            other.exchange_money(self.__currency)
            self.__amount = self.__amount / other.__amount

    def __eq__(self, other):
        if self.__currency == other.__currency and self.__amount == other.__amount:
            return True
        elif self.__currency != other.__currency and self.__amount != other.__amount:
            other.exchange_money(self.__currency)
            if self.__amount == other.__amount:
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        if self.__currency != other.__currency and self.__amount == other.__amount:
            return True
        elif self.__currency == other.__currency and self.__amount == other.__amount:
            return True
        elif self.__currency == other.__currency and self.__amount == other.__amount:
            return False
        elif self.__currency != other.__currency and self.__amount != other.__amount:
            other.exchange_money(self.__currency)
            if self.__amount != other.__amount:
                return True
            else:
                return False

    def __lt__(self, other):
        if self.__currency == other.__currency and self.__amount > other.__amount:
            return True
        elif self.__currency != other.__currency and self.__amount != other.__amount:
            other.exchange_money(self.__currency)
            if self.__amount > other.__amount:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.__currency == other.__currency and self.__amount < other.__amount:
            return True
        elif self.__currency != other.__currency and self.__amount != other.__amount:
            other.exchange_money(self.__currency)
            if self.__amount < other.__amount:
                return True
            else:
                return False
        else:
            return False

    def __le__(self, other):
        if self.__currency == other.__currency and self.__amount <= other.__amount:
            return True
        elif self.__currency != other.__currency and self.__amount != other.__amount:
            other.exchange_money(self.__currency)
            if self.__amount <= other.__amount:
                return True
            else:
                return False
        else:
            return False

    def __ge__(self, other):
        if self.__currency == other.__currency and self.__amount >= other.__amount:
            return True
        elif self.__currency != other.__currency and self.__amount != other.__amount:
            other.exchange_money(self.__currency)
            if self.__amount >= other.__amount:
                return True
            else:
                return False
        else:
            return False


# m = Money(5800, 'AMD')
# m.exchange_money('EUR')

# m = Money(400, 'USD')
# m.exchange_money('AMD')
# print(m.__repr__())
# m.exchange_money('EUR')
# print(m.__repr__())
# m.exchange_money('RUB')
# print(m.__repr__())

# print(m.__repr__())
# m.currency = 'EUR'
# print(m.__repr__())


class Doctor(Person):
    def __init__(self, name, surname, gender, age, address, friends, job, department, profession, patronymic, salary):
        super().__init__(name, surname, gender, age, address, friends, job)
        self.__department = department
        self.__profession = profession
        self.__patronymic = patronymic
        self.__salary = salary

    def __repr__(self):
        return "Full name: {} {},\nGender: {}\nAge: {}\nAddress: {},\nJobs: {}\nFriends: " \
               "{}\nDepartment: {}\nProfession: {}\nPatronymic: {}\nSalary: {}".format(self.person_name,
                                                                                       self.person_surname,
                                                                                       self.person_gender,
                                                                                       self.person_age,
                                                                                       self.person_address,
                                                                                       self.person_job,
                                                                                       self.person_friends,
                                                                                       self.__department,
                                                                                       self.__profession,
                                                                                       self.__patronymic,
                                                                                       self.__salary)

    @property
    def department(self):
        return self.__department

    @property
    def profession(self):
        return self.__profession

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def salary(self):
        return self.__salary

    @department.setter
    def department(self, other):
        self.__department = other

    @profession.setter
    def profession(self, other):
        self.__profession = other

    @patronymic.setter
    def patronymic(self, other):
        self.__patronymic = other

    @salary.setter
    def salary(self, other):
        self.__salary = other


# d = Doctor('Anna', 'Dabaghyan', 'Female', 27, 'Abovyan', [None], ['Nurse', 'Doctor'], 'Gastroenterology',
#            'Gastroenterologist', 'Samvel', 100 )
#
# print(d.__repr__())


class Teacher(Person):
    def __init__(self, name, surname, gender, age, address, friends, job, university, faculty, experience,
                 start_work_at, subject, salary):
        super().__init__(name, surname, gender, age, address, friends, job)
        self.__university = university
        self.__faculty = faculty
        self.__experience = experience
        self.__start_work_at = start_work_at
        self.__subject = subject
        self.__salary = salary

    def __repr__(self):
        return "Full name: {} {}\nGender: {}\nAge: {}\nAddress: {}\nFriends: " \
               "{}\nJobs: {}\nUniversity: {}\nFaculty: {}\nExperience: {}\nStarting {}\nSubject: {}\nSalary:{}" \
               "".format(self.person_name,
                         self.person_surname,
                         self.person_gender,
                         self.person_age,
                         self.person_address,
                         self.person_job,
                         self.person_friends,
                         self.__university,
                         self.__faculty,
                         self.__experience,
                         self.__start_work_at,
                         self.__subject,
                         self.__salary)

    @property
    def experience(self):
        return self.__experience

    @property
    def start_work_at(self):
        return self.__start_work_at

    @property
    def subject(self):
        return self.__subject

    @property
    def faculty(self):
        return self.__faculty

    @property
    def salary(self):
        return self.__salary

    @experience.setter
    def experience(self, other):
        self.__experience = other

    @faculty.setter
    def faculty(self, other):
        self.__faculty = other

    @salary.setter
    def salary(self, other):
        self.__salary = other


# t = Teacher('Anna', 'Dabaghyan', 'Female', 27, 'Abovyan', ['Nurse', 'Doctor'], [None], 'YSU',
#            'Economics', 10, Date(1,1,2013), 'Theory of Economics', 100)
#
# print(t.__repr__())


class Student(Person):
    def __init__(self, name, surname, gender, age, address, friends, job, university, faculty, course, started_at):
        super().__init__(name, surname, gender, age, address, friends, job)
        self.__university = university
        self.__faculty = faculty
        self.__course = course
        self.__started_at = started_at

    def __repr__(self):
        return "Full name: {} {}\nGender: {}\nAge: {}\nAddress: {}\nFriends: " \
               "{}\nJobs: {}\nUniversity: {}\nFaculty: {}\nExperience: {}\nStarting {}\n".format(self.person_name,
                                                                                                 self.person_surname,
                                                                                                 self.person_gender,
                                                                                                 self.person_age,
                                                                                                 self.person_address,
                                                                                                 self.person_job,
                                                                                                 self.person_friends,
                                                                                                 self.__university,
                                                                                                 self.__faculty,
                                                                                                 self.__course,
                                                                                                 self.__started_at)

    @property
    def university(self):
        return self.__university

    @property
    def faculty(self):
        return self.__faculty

    @property
    def course(self):
        return self.__course

    @property
    def started_at(self):
        return self.__started_at

    @university.setter
    def university(self, other):
        self.__university = other

    @faculty.setter
    def faculty(self, other):
        self.__faculty = other

    @course.setter
    def course(self, other):
        self.__course = other


class University:
    def __init__(self, name, founded_at, director, city):
        self.__name = name
        self.__founded_at = founded_at
        self.__director = director
        self.__city = city

    def __repr__(self):
        return "Name:{}\nFounded {}\nDirector:{}\nCity:{}".format(self.__name, self.__founded_at, self.__director,
                                                                  self.__city)

    @property
    def name(self):
        return self.__name

    @property
    def founded_at(self):
        return self.__founded_at

    @property
    def director(self):
        return self.__director

    @property
    def city(self):
        return self.__city

    @name.setter
    def name(self, other):
        self.__name = other

    @director.setter
    def director(self, other):
        self.__director = other


class cityError(Exception):
    def __init__(self, population):
        self.__population = population

    def __str__(self):
        if self.__population is not int:
          return 'Population parameter can be only int type'


class City:
    def __init__(self, name, mayor, population, language):
        self.__name = name
        self.__mayor = mayor
        self.__language = language
        self.__population = population
        try:
            raise cityError
        except:
            cityError(self.__population)


    # @staticmethod
    # def count_calls(func):
    #     def wrapper(*args, **kwargs):
    #         wrapper.count += 1
    #         result = func(*args, **kwargs)
    #         print("{} was called {} times".format(func().__name__, wrapper.count))
    #         return result
    #
    #     wrapper.count = 0
    #     return wrapper

    def __repr__(self):
        return "Name:{}\nMayor:{}\nPopulation:{}\nLanguage:{}".format(self.__name, self.__mayor, self.__population,
                                                                      self.__language)

    @property
    def name(self):
        return self.__name

    @property
    def mayor(self):
        return self.__mayor

    @property
    def population(self):
        return self.__population

    # @count_calls
    @property
    def language(self):
        return self.__language

    @name.setter
    def name(self, other):
        self.__name = other

    @mayor.setter
    def mayor(self, other):
        self.__mayor = other

    # @count_calls
    @population.setter
    def population(self, other):
        self.__population = other


c = City('Abovyan', 'Hakob Hakobyan', '5', 'Armenian')
print(c.population)
print(c.language)


class MyRange:
    def __init__(self, end, current=0, step=1):
        self.__current = current
        self.__end = end
        self.__step = step

    def __repr__(self):
        return f"MyRange({self.__end}, {self.__current}, {self.__step})"

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current >= self.__end:
            raise StopIteration
        i = self.__current
        self.__current += self.__step
        return i

    def __len__(self):
        return (self.__end - self.__current) // self.__step

    def __getitem__(self, index):
        return self.__current + index * self.__step

    def __reversed__(self):
        return MyRange(self.__current + (len(self) - 1) * self.__step, self.__current, -self.__step)


r = MyRange(10)
# print(next(r))
# print(next(r))
# print(next(r))
# print(len(r))
# print(r[3])

# for i in r:
#     print(i)
