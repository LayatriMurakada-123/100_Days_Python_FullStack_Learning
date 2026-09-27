# ============================================================
# Employee Management System using Python OOP
# ============================================================


# ---------------- Employee ---------------- #

class Employee:

    company_name = "Codegnan Technologies"   # Class Attribute
    employee_count = 0

    def __init__(self, name, age, emp_id, Edu_BG, Gender, Department, salary):
        self.__name = name                    # Encapsulation
        self.age = age
        self.__emp_id = emp_id                # Encapsulation
        self.Edu_BG = Edu_BG
        self.Gender = Gender
        self.Department = Department
        self.salary = salary

        Employee.employee_count += 1

    # ---------------- Display Method ---------------- #

    def display_info(self):
        print("\n------ Employee Details ------")
        print("Company    :", Employee.company_name)
        print("Name       :", self.__name)
        print("Age        :", self.age)
        print("Employee ID:", self.__emp_id)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)
        print("Salary     :", self.salary)

    # ---------------- Encapsulation ---------------- #

    def get_name(self):
        return self.__name

    def get_employee_id(self):
        return self.__emp_id

    # ---------------- Polymorphism ---------------- #

    def details(self):
        print("This is a general Employee.")

    # ---------------- Static Method ---------------- #

    @staticmethod
    def company_policy():
        print("\nCompany Policy:")
        print("Employees must follow company rules and regulations.")

    # ---------------- Class Method ---------------- #

    @classmethod
    def total_employees(cls):
        print("Total Employees :", cls.employee_count)

    # ---------------- Operator Overloading ---------------- #

    def __str__(self):
        return f"{self.__name} - {self.__emp_id} - {self.salary}"

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary


# ============================================================
# Manager
# ============================================================

class Manager(Employee):

    manager_count = 0

    def __init__(
        self,
        name,
        age,
        emp_id,
        Edu_BG,
        Gender,
        Department,
        salary,
        team_size
    ):

        super().__init__(
            name,
            age,
            emp_id,
            Edu_BG,
            Gender,
            Department,
            salary
        )

        self.team_size = team_size

        Manager.manager_count += 1

    # Method Overriding
    def details(self):
        print("\n------ Manager Details ------")
        print("Name       :", self.get_name())
        print("Employee ID:", self.get_employee_id())
        print("Department :", self.Department)
        print("Salary     :", self.salary)
        print("Team Size  :", self.team_size)

    @classmethod
    def total_managers(cls):
        print("Total Managers :", cls.manager_count)


# ============================================================
# Developer
# ============================================================

class Developer(Employee):

    developer_count = 0

    def __init__(
        self,
        name,
        age,
        emp_id,
        Edu_BG,
        Gender,
        Department,
        salary,
        programming_language
    ):

        super().__init__(
            name,
            age,
            emp_id,
            Edu_BG,
            Gender,
            Department,
            salary
        )

        self.programming_language = programming_language

        Developer.developer_count += 1

    # Method Overriding
    def details(self):
        print("\n------ Developer Details ------")
        print("Name       :", self.get_name())
        print("Employee ID:", self.get_employee_id())
        print("Department :", self.Department)
        print("Salary     :", self.salary)
        print("Programming Language :", self.programming_language)

    @classmethod
    def total_developers(cls):
        print("Total Developers :", cls.developer_count)


# ============================================================
# HR
# ============================================================

class HR(Employee):

    hr_count = 0

    def __init__(
        self,
        name,
        age,
        emp_id,
        Edu_BG,
        Gender,
        Department,
        salary,
        experience
    ):

        super().__init__(
            name,
            age,
            emp_id,
            Edu_BG,
            Gender,
            Department,
            salary
        )

        self.experience = experience

        HR.hr_count += 1

    # Method Overriding
    def details(self):
        print("\n------ HR Details ------")
        print("Name       :", self.get_name())
        print("Employee ID:", self.get_employee_id())
        print("Department :", self.Department)
        print("Salary     :", self.salary)
        print("Experience :", self.experience, "years")

    @classmethod
    def total_hr(cls):
        print("Total HR Employees :", cls.hr_count)


# ============================================================
# Tester
# ============================================================

class Tester(Employee):

    tester_count = 0

    def __init__(
        self,
        name,
        age,
        emp_id,
        Edu_BG,
        Gender,
        Department,
        salary,
        testing_tool
    ):

        super().__init__(
            name,
            age,
            emp_id,
            Edu_BG,
            Gender,
            Department,
            salary
        )

        self.testing_tool = testing_tool

        Tester.tester_count += 1

    # Method Overriding
    def details(self):
        print("\n------ Tester Details ------")
        print("Name       :", self.get_name())
        print("Employee ID:", self.get_employee_id())
        print("Department :", self.Department)
        print("Salary     :", self.salary)
        print("Testing Tool :", self.testing_tool)

    @classmethod
    def total_testers(cls):
        print("Total Testers :", cls.tester_count)


# ============================================================
# Accountant
# ============================================================

class Accountant(Employee):

    accountant_count = 0

    def __init__(
        self,
        name,
        age,
        emp_id,
        Edu_BG,
        Gender,
        Department,
        salary,
        accounting_software
    ):

        super().__init__(
            name,
            age,
            emp_id,
            Edu_BG,
            Gender,
            Department,
            salary
        )

        self.accounting_software = accounting_software

        Accountant.accountant_count += 1

    # Method Overriding
    def details(self):
        print("\n------ Accountant Details ------")
        print("Name       :", self.get_name())
        print("Employee ID:", self.get_employee_id())
        print("Department :", self.Department)
        print("Salary     :", self.salary)
        print("Accounting Software :", self.accounting_software)

    @classmethod
    def total_accountants(cls):
        print("Total Accountants :", cls.accountant_count)


# ============================================================
# Objects
# ============================================================

employee1 = Employee(
    "Rahul Sharma",
    25,
    "E001",
    "B.Tech",
    "Male",
    "Operations",
    30000
)

employee2 = Employee(
    "Ananya Reddy",
    24,
    "E002",
    "B.Com",
    "Female",
    "Administration",
    30000
)


manager1 = Manager(
    "Ravi Kumar",
    40,
    "M001",
    "MBA",
    "Male",
    "Management",
    70000,
    15
)

manager2 = Manager(
    "Meera Srinivas",
    38,
    "M002",
    "MBA",
    "Female",
    "Management",
    65000,
    10
)


developer1 = Developer(
    "Arjun",
    28,
    "D001",
    "B.Tech",
    "Male",
    "Development",
    60000,
    "Python"
)

developer2 = Developer(
    "Geetha",
    26,
    "D002",
    "MCA",
    "Female",
    "Development",
    55000,
    "Java"
)


hr1 = HR(
    "Priya",
    32,
    "H001",
    "MBA",
    "Female",
    "Human Resources",
    45000,
    7
)

hr2 = HR(
    "Kiran",
    35,
    "H002",
    "MBA",
    "Male",
    "Human Resources",
    48000,
    9
)


tester1 = Tester(
    "Suresh",
    29,
    "T001",
    "B.Tech",
    "Male",
    "Testing",
    50000,
    "Selenium"
)

tester2 = Tester(
    "Lakshmi",
    27,
    "T002",
    "B.Tech",
    "Female",
    "Testing",
    52000,
    "PyTest"
)


accountant1 = Accountant(
    "Ramesh",
    42,
    "A001",
    "M.Com",
    "Male",
    "Finance",
    45000,
    "Tally"
)

accountant2 = Accountant(
    "Seetha",
    36,
    "A002",
    "M.Com",
    "Female",
    "Finance",
    47000,
    "Excel"
)


# ============================================================
# Output
# ============================================================

print("\n================================================")
print("       EMPLOYEE MANAGEMENT SYSTEM")
print("================================================")


# ---------------- Employee Details ---------------- #

employee1.display_info()
employee2.display_info()


# ---------------- Manager Details ---------------- #

manager1.details()
manager2.details()


# ---------------- Developer Details ---------------- #

developer1.details()
developer2.details()


# ---------------- HR Details ---------------- #

hr1.details()
hr2.details()


# ---------------- Tester Details ---------------- #

tester1.details()
tester2.details()


# ---------------- Accountant Details ---------------- #

accountant1.details()
accountant2.details()


# ============================================================
# Encapsulation
# ============================================================

print("\n------ Encapsulation ------")

print("Employee Name :", employee1.get_name())
print("Employee ID   :", employee1.get_employee_id())


# ============================================================
# Static Method
# ============================================================

Employee.company_policy()


# ============================================================
# Class Methods
# ============================================================

print("\n------ Employee Counts ------")

Employee.total_employees()
Manager.total_managers()
Developer.total_developers()
HR.total_hr()
Tester.total_testers()
Accountant.total_accountants()


# ============================================================
# Polymorphism
# ============================================================

print("\n------ Polymorphism ------")

employees = [
    employee1,
    manager1,
    developer1,
    hr1,
    tester1,
    accountant1
]

for emp in employees:
    emp.details()


# ============================================================
# Operator Overloading
# ============================================================

print("\n------ Operator Overloading ------")

print("\n__str__ Operator:")
print(employee1)
print(manager1)
print(developer1)


print("\n__eq__ Operator:")

if employee1 == employee2:
    print("Employee 1 and Employee 2 have the same salary.")
else:
    print("Employee 1 and Employee 2 have different salaries.")


print("\n__lt__ Operator:")

if employee1 < manager1:
    print("Employee 1 salary is less than Manager 1 salary.")
else:
    print("Employee 1 salary is not less than Manager 1 salary.")


print("\n__gt__ Operator:")

if manager1 > developer1:
    print("Manager 1 salary is greater than Developer 1 salary.")
else:
    print("Manager 1 salary is not greater than Developer 1 salary.")
