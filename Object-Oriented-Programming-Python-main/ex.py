class Employee:
    raise_amt=1.5
    def __init__(self,name,last,empid,pay):
        self.name=input("Enter employee's first name:")
        self.last=input("Enter last name:")
        self.empid=int(input("Enter EMPID:"))
        self.pay=int(input("Enter net salary:"))

    def raaise(self):
        return self.raise_amt*self.pay
    
    def show(self):
        print("The name of the employee is "+self.name+self.last)
        print("Employee ID:",self.empid)
        print("Initial Pay:",self.pay) 
        print("Upon raise:",self.raaise())   


class Developer(Employee):
    raise_amt=3

    def raaise(self):
        return (int(self.raise_amt)*100)/self.pay+self.pay

class Manager(Employee):
    raise_amt=2
    def raaise(self):
        return (int(self.raise_amt)*100)/self.pay+self.pay

e1=Developer("Chaya","Rao",6789,50000)
e2=Employee("Eeshan","Lothal",7935,50000)    
e1.show()
e2.show()
