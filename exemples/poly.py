class Animal:
    def talk(self):
        print(f"{self.__class__.__name__} : Waf")

class Dog(Animal):
    ...

class Cat(Animal):
    def talk(self):
        print("Miaou")

def make_animal_talk(animal):
    animal.talk()

animal = Dog()
make_animal_talk(animal)
