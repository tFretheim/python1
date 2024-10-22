
class Student:
    passingMark = 50  

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark


     # String representation of the object
    def __str__(self):
        return f"Name: {self.name}, Mark: {self.mark}"

    #Method to determine if student passes or fails
    def passOrFail(self):
        if self.mark >= self.passingMark:
            return f"{self.name} passed with {self.mark} marks"
        else:
            return f"{self.name} failed with {self.mark} marks"


#Instance creation for class: Student
student1 = Student("John", 52)
status1 = student1.passOrFail()
print("Status for student1:", status1) #Student1 Statuscheck

student2 = Student("Jenny", 69)
status2 = student2.passOrFail()
print("Status for student2:", status2) #Student2 Statuscheck

#Mark update
Student.passingMark = 60


#Status-check
status1 = student1.passOrFail()
status2 = student2.passOrFail()

print("Status for student1 after updating passingMark:", status1)
print("Status for student2 after updating passingMark:", status2)
