employees = []

class Employee():
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

def newemployee(dep):
    print("Put name")
    n = input()
    print("Put salary")
    s = int(input())
    d = dep
    if dep == 0:
        print("Put department")
        d = int(input())
    e = Employee(n,s,d)
    employees.append(e)
    print("New employee",e.name,"was added in department",e.department,"with salary",e.salary)

def giveemloyeeslist(dep, withnumbers = False):
    if len(employees) > 0:
        iter = 0
        for i in employees:
            if i.department == dep:
                if withnumbers:
                    print("#",iter, i.name)
                else:
                    print(i.name)
            elif dep == 0:
                if withnumbers:
                    print("#",i.name,"department #",i.department)
                else:
                    print(i.name,"department #",i.department)
            iter += 1

def givesalarylist(dep):
    if len(employees) > 0:
        for i in employees:
            if i.department == dep or dep == 0:
                print(i.name,i.salary)  

def salarystats(dep):
    sum = 0
    count = 0
    if len(employees) > 0:
        for i in employees:
            if i.department == dep or dep == 0:
                sum += i.salary
                count += 1
    if dep > 0:
        print("In department #",dep)
    print("Sum is", sum)
    print("Average salary is", sum/count)

def minandmaxsalary(dep):
    if len(employees) > 0:
        minsalary = employees[0].salary
        maxsalary = employees[0].salary
        imin = 0
        imax = 0
        iter = 0
        for i in employees:
            if i.department == dep or dep == 0:
                if i.salary < minsalary:
                    imin = iter
                    minsalary = i.salary
                if i.salary > maxsalary:
                    imax = iter
                    maxsalary = i.salary
            iter += 1
        if dep > 0:
            print("In department #",dep)
        print(employees[imin].name, "has the lowest salary, only", employees[imin].salary)
        print(employees[imax].name, "has the highest salary, it's", employees[imax].salary)

def raisesalaries(dep):
    if len(employees) > 0:
        print("put persentage of raise")
        p = 1 + int(input())/100
        for i in employees:
            if i.department == dep or dep == 0:
                i.salary *= p
        givesalarylist(dep)

def removeemployee(dep):
    giveemloyeeslist(dep,True)
    print("Send # of employee to delete")
    i = int(input())
    name = employees[i].name
    employees.pop(i)
    print(name, "left our company. Bye-bye!")

def startmessage():
    print("Hi! Select the department or send 0 to work with every employee")
    dep = int(input())

    print("Send 1 to input a new employee!")
    print("Send 2 to get a list of employees!")
    print("Senf 3 to find total expenses and average salary")
    print("Send 4 to find minimum and maximum salary")
    print("Send 5 to raise wages")
    print("Send 6 to get stats for department")
    print("Send 7 to remove employee")
    
    newinput = int(input())
    if newinput == 1:
        newemployee(dep)
    elif newinput == 2:
        giveemloyeeslist(dep)
    elif newinput == 3:
        salarystats(dep)
    elif newinput == 4:
        minandmaxsalary(dep)
    elif newinput == 5:
        raisesalaries(dep)
    elif newinput == 6:
        givesalarylist(dep)
    elif newinput == 7:
        removeemployee(dep)
    startmessage()

employees.append(Employee("Azamat",250000,1))
employees.append(Employee("Lida",95000,1))
employees.append(Employee("Andrey",195000,1))
employees.append(Employee("Diana",45000,2))
employees.append(Employee("Ruslan",35000,2))
employees.append(Employee("Alex",735000,3))

startmessage()