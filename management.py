class Employee:
    employee_list = []

    def __init__(self, num, Empname, salary, email):
        self.num, self.Empname, self.salary, self.email = num, Empname, salary, email

    def setnum(self, num):
        self.num = num

    def getnum(self):
        return self.num

    def setEmpname(self, Empname):
        self.Empname = Empname

    def getEmpname(self):
        return self.Empname

    def setsalary(self, salary):
        self.salary = salary

    def getsalary(self):
        return self.salary

    def setemail(self, email):
        self.email = email

    def getemail(self):
        return self.email

    def __repr__(self):
        return f'<Employee: {self.email}>'


class Manager(Employee):

    def __init__(self, num, Empname, salary, email, employee=[]):
        super().__init__(num, Empname, salary, email)
        self.person_all = []

    def add_employee(self):

        choice = 1
        while choice >= 1 and choice <= 3:
            print("1. Add New Employee\n2. Employee Directory\n3. Remove Employee :")
            choice = int(input("Enter Your Choice : "))
            if(choice == 1):
                num = int(input("Enter Employee No: "))
                Empname = input("Enter Employee Name: ")
                salary = float(input("Enter Employee Salary: "))
                email = input("Enter Employee Email")
                self.person_all.append(self)

            elif(choice == 2):
                print("\n")
                Empname = input("Enter Employee name: ")
                self.person_all

            elif(choice == 3):
                print("\n")
                self.person_all.remove(self)
            
            


# My_manager = Manager(5478, "Andrew Ratliff", 65000, "joedoe@joedoe.com")
# My_manager.add_employee()
