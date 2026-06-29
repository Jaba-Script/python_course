class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        
    def get_details(self):
        print(f"Сотрудник: {self.name}, Зарплата: {self._salary}")            
            
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        
    def get_details(self):
        print(f"Сотрудник: {self.name}, Зарплата: {self._salary}, Отдел: {self.department}")

            
Employee1 = Employee(name='Ivan', salary=1500)
Manager1 = Manager(name='Vova', salary=2500, department="IT")

Employee1.get_details()
Manager1.get_details()

        
#1) _User__password
#2) _password python технически разрешает доступ (сделано для разработчиков), __password польностю блокирует доступ снаружи 