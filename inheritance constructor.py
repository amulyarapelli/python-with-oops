class Demo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Sample(Demo):
    def info(self):
        print(self.name)
        print(self.age)

sam1 = Sample("abc", 12)
sam1.info()
sam2 = Sample("chd", 11)
sam2.info()
