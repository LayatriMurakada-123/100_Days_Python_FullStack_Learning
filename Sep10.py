'''
Scenerio to understand (*args and **kwargs)
Modules --> Some interesting cases -> Projects (Virtual Assistant, Email Automation)
OOP --> Github (branch)

#Employee Details

def employees(*names,**settings):
    """Employee Details along with their Settings"""       
    print("Employee Names")
    for employee in names:
        print('_________')
        print('_',employee)

    for key,value in settings.items():
        print("Key is",key)
        print("Value is",value)

employees("Rahul","Akash","Saritha",
          department = "Operations",
          experience_letters = True,
          Salary = True)


Projects

Module --> A Module is a simple python file(reusable,organized code)

import keyword

OOP

Organization --> Class

Encapsulation, Inheritance, Polymorphism

Employees --> Function(methods)
Performanance Metrices --> Function
Increment --> Function

Emp1,Emp2,Emp3,...... --> Objects

'''

#Employee Details

def employees(*names,**settings):
    """Employee Details along with their Settings"""       
    print("Employee Names")
    for employee in names:
        print('_________')
        print('_',employee)

    for key,value in settings.items():
        print("Key is",key)
        print("Value is",value)

employees("Rahul","Akash","Saritha",
          department = "Operations",
          experience_letters = True,
          Salary = True)

#if __name__ == "__main__":

details = {'Organization':'Codegnan',
           'year':2018,
           'branches':['Vijayawada','Hyderabad','Vizag']}

print(__name__) #Dunder methods --> Magic methods






































