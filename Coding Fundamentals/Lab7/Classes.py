class Student:
	def __init__(self,namevar,agevar,classroomvar,test1,test2,test3):
		self.name = namevar
		self.age = agevar
		self.classroom = classroomvar
		self.test1 = test1
		self.test2 = test2
		self.test3 = test3

	def averagestestscore(self):
		#average = (self.test1 + self.test2 + self.test3 / 3)
		return self.test1 + self.test2 + self.test3 / 3
		

	

student1 = Student('WhiplashPrince', 15, 'Maths', 50, 60, 90)
student2 = Student('BillyBob', 16, 'English', 30, 20, 80)

print (student1.age)
print ('Age:',student2.age, 'Class:',student2.classroom, 'Average Test Score:',student2.averagestestscore())
