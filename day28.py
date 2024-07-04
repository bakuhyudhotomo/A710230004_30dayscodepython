class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_salary(self, salary):
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

# Membuat objek Employee
employee1 = Employee("John Doe", 30, 5000)

# Mengakses dan memodifikasi atribut menggunakan method
print("Employee Name:", employee1.get_name())
print("Employee Age:", employee1.get_age())
print("Employee Salary:", employee1.get_salary())

employee1.set_name("Jane Doe")
employee1.set_age(35)
employee1.set_salary(6000)

print("\nAfter Modification:")
print("Employee Name:", employee1.get_name())
print("Employee Age:", employee1.get_age())
print("Employee Salary:", employee1.get_salary())
