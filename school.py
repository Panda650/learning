class Student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_info(self):
        print(self.name, self.gender)


class Stage(Student):
    def __init__(self, name, gender, stage):
        self.stage = stage
        super().__init__(name, gender)
        
    def get_info(self):
        super().get_info()
        print("stage is ", self.stage)


hasan = Stage("hasan safaa", "male", 3)
hasan.get_info()
