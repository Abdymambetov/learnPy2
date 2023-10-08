class A:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Объект {self.name} класса А, возраст {self.age}"
    
a1 = A('Meder', 18)
print(a1)

a2 = A('Erika', 19)
print(str(a2))