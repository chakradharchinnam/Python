class Employee:

    emp_count=0

    sum=0

    average=0

    def __init__(self, empname, sal, dept):

        self.empname=empname

        self.sal=sal

        Employee.emp_count+=1

        Employee.sum+=self.sal

        self.dept=dept

class Fulltime_Employee(Employee):

    def __init__(self,n,s,d):

        Employee.__init__(self,n,s,d)

employee1 = Employee("vicky",2000,10)

employee2 = Employee("chakradhar",4000,20)

employee3 = Employee("chinnam",6000,10)

employee4 = Employee("raj",8000,10)

employee5 = Employee("prakash",10000,20)

employee6 = Employee("venkat",12000,10)

# prints total number of empolyees
print("total number of employees:",Fulltime_Employee.emp_count)

#Prints the Average salary of the employee
print("Average salary of the employees is", (Employee.sum/Employee.emp_count))