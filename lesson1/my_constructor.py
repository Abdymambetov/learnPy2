

class Cat():
    def __init__(self, cat_name):
        self.name = cat_name
    tail = 1
    paws = 4

    def say(self):
        print('Meow')

class Tiger(Cat):
    color = 'striped'
    def say(self):
        print('Arr')

class WhiteTiger(Tiger):
    color = 'white striped'

gatsby = WhiteTiger('great gatsby')
gatsby.say()
print(gatsby.color)
print(gatsby.paws)
# bars = Cat('Bars')
# bars.say()
# print(bars.tail)
# print(bars.paws)

# m = Cat('Medik')
# print(m.paws)
# m.say()