class Student:
    name = "Student Name"
    course = "Course Name"
    college = "College Name"
    examRoll = 0

    def getInfo(self):
        print(f"{self.name} is a  {self.course} student in {self.college}. Roll No = {self.examRoll}")

    
aman = Student()

aman.name = "Aman Kumar Sinha"
aman.course = "BCA"
aman.college = "R.N. College, Hajipur"
aman.examRoll = 213184


print(aman.name) # Aman Kumar Sinha
print(aman.course) # BCA
print(aman.college) # R.N. College, Hajipur
print(aman.examRoll) # 213184


aman.getInfo()
# Aman Kumar Sinha is a  BCA student in R.N. College, Hajipur. Roll No = 213184


anand = Student()

anand.name = "Anand Jha"
anand.course = "BCA"
anand.college = "R.N. College, Hajipur"
anand.examRoll = 213102

anand.getInfo()
# Anand Jha is a  BCA student in R.N. College, Hajipur. Roll No = 213102