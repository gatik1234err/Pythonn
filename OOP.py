class Student:
    roll_number = 9

    def __init__(self, roll_number):
        self.roll_number = roll_number

    def learn(self):
        return "learning ..."

    def bunk(self):
        pass


gatik = Student(24)
print(gatik.roll_number)
print(gatik.learn())


class Faculty:
    def __init__(self):
        self.skills = []

    def teach(self):
        return "Teaching"


prasad = Faculty()
prasad.skills = ["python", "js"]
print(prasad.skills)
print(prasad.teach())

gatik = Faculty()
Faculty.skills = ["SV"]
print(gatik.skills)
