class Employee():
	leaves = 8
	print("class create object")
	
	def __init__(self,aname,asalary):
		self.name = aname
		self.salary = asalary
		
	def printdetails(self):
		print("Name:-",self.name,",","Salary:-",self.salary,",","Leaves:-",self.leaves)
	
	@classmethod
	def changeleaves(cls,newleaves):
		cls.leaves = newleaves
	
	
	
E1 = Employee("Parth",10000)
E2 = Employee("Jaimin",104000)
E1.changeleaves(25)
print(E1.__dict__)
print(E1.leaves)
print(Employee.leaves)
E1.leaves = 5
print(E1.leaves)
print(E2.leaves)
print(Employee.leaves)