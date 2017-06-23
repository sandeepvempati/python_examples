class Employee:

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = self.fname + '.' + self.lname + "@company.com"

class Developer(Employee):
    pass

emp = Developer('sandeep','vempati',70000)
print emp.email

list = [1,2,3,5,8,9,8,7]
print list.extend([5,2,3])
print max(list)