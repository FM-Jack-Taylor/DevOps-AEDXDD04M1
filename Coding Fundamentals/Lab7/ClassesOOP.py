from abc import ABC, abstractmethod

class Bird:
    birds = 0
    def newbird(self):
        self.birds += 1
    @abstractmethod
    def food(self):# abstraction
        pass

class Owl(Bird):# inheritance
    def newowls(self):
        self.birds += 1

    def food(self):
        return 'I eat invertebrates'

class Dodo(Bird):# inheritance
    def newdodos(self):
        self.birds += 5

    def food(self):
        return 'I eat nuts and seeds'
 

bird1 = Owl()
bird2 = Dodo()
print(bird1.birds)
print(bird2.birds)
bird1.newbird()
bird2.newdodos()
bird2.newdodos()
print(bird1.birds)
print(bird2.birds)

for food in (bird1, bird2): #polymorphism
    print(food.food())


