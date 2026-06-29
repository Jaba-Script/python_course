#Я добавил функционал и чучуть поменял значени. Смысл задания по идее остался
class Car:
    def __init__(self, brand, model, fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        
    def drive(self, distance): #езда
        cur_dist = 0
        while cur_dist != distance and self.fuel != 0:
            cur_dist += 1
            self.fuel -= 1
            if cur_dist % 100 == 0:
                self.refuel(20)
                print(f"Проехали {cur_dist} км. Заправились на 20л. Текущее топливо: {round(self.fuel)} л.")
        else:
            if cur_dist == distance:
                print(f"Проехали {distance} км. Осталось топлива: {round(self.fuel)} л.")
            elif self.fuel == 0:
                print(f"Закончилось топливо! Проехали {cur_dist} км.")
                #Одобрение на заправку
                while True:
                    agree = input("Желаете заправится?(y/n): ")
                    if agree == "y":
                        liters = check_int("Введите количество литров: ")
                        self.refuel(liters=liters)
                        print(f"Текущее топливо: {round(self.fuel)}")
                        
                        #Одобрение на продолжение пути
                        while True:
                            drive_agree = input("Желаете продолжить путь?(y/n): ")
                            if drive_agree == "y":
                                self.drive(distance=distance - cur_dist)
                                break
                            elif drive_agree == 'n':
                                print(f"Всего проехали {cur_dist} км.")
                                break
                            else:
                                print("Неверная команда!")
                        break                         
                        
                        
                    elif agree == 'n':
                        print(f"Всего проехали {cur_dist} км.")
                        break
                    else:
                        print("Неверная команда!")
                        
        
    def refuel(self, liters): # Заправка
        self.fuel += liters
        
            
def check_int(text):
    while True:
        try:
            data = int(input(text))
            break
        except ValueError:
            print("Введите число!")
    return data

Dodge = Car(brand="Dodge", model="GT", fuel=100)
distance = check_int("Введите длинну маршрута: ")
Dodge.drive(distance)

#1) метод __init__ нужен для установления характеристик класа
#2) не понял