class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks>=40:
            return "Pass"
        else:
            return "Fail"

s1 = Student("Nabin" , 69)
print(f"{s1.name}: {s1.result()}")

s2 = Student("Richard" , 36)
print(f"{s2.name}: {s2.result()}")

s3 = Student("Finley" , 67)
print(f"{s3.name}: {s3.result()}")