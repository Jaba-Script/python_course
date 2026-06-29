class Dog:
    def __init__(self, name):
        self.name = name
        
    def make_sound(self):
        return f"{self.name} гооврит: Гав-гав!"    
    
    def __str__(self):
        return f"Собаку зовут: {self.name}"     
            
class Cat:
    def __init__(self, name):
        self.name = name
        
    def make_sound(self):
        return f"{self.name} гооврит: Мяу!"
        
    def __str__(self):
        return f"Кошку зовут: {self.name}" 

            
animals = [Dog("Карапуз"), Cat("Куки"), Dog("Печкин")]

for animal in animals:
    print(animal)
    print(animal.make_sound())

        
#1) Магические методы (можешь дать визначення)
#2) Необезательно, нужно чтобы совпадало имя метода