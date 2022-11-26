employees = []

class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

def newemployee():
    print("Put name")
    n = input()
    print("Put salary")
    s = int(input())
    e = Employee(n,s)
    employees.append(e)
    print("New employee was added!")
    startmessage()

def giveemloyeeslist():
    if len(employees) > 0:
        for i in employees:
            print(i.name)
    startmessage()

def salarystats():
    sum = 0
    if len(employees) > 0:
        for i in employees:
            sum += i.salary
    print("Sum is", sum)
    print("Average salary is", sum/len(employees))
    startmessage()

def minandmaxsalary():
    if len(employees) > 0:
        minsalary = employees[0].salary
        maxsalary = employees[0].salary
        imin = 0
        imax = 0
        iter = 0
        for i in employees:
            if i.salary < minsalary:
                imin = iter
                minsalary = i.salary
            if i.salary > maxsalary:
                imax = iter
                maxsalary = i.salary
            iter += 1
        print(employees[imin].name, "has the lowest salary, only", employees[imin].salary)
        print(employees[imax].name, "has the highest salary, it's", employees[imax].salary)
    startmessage()

def startmessage():
    print("Hi!")
    print("Send 1 to input a new employee!")
    print("Send 2 to get a list of employees!")
    print("Senf 3 to find total expenses and average salary")
    print("Senf 4 to find minimum and maximum salary")
    
    newinput = int(input())
    if newinput == 1:
        newemployee()
    elif newinput == 2:
        giveemloyeeslist()
    elif newinput == 3:
        salarystats()
    elif newinput == 4:
        minandmaxsalary()

startmessage()