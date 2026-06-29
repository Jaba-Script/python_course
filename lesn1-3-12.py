class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        
    def get_password(self):
        return len(self.__password) * '*'
    
    def set_password(self, new_password):
        if len(new_password) < 6:
            print('Пароль слишком короткий!')
        else:
            self.__password = new_password
            
            
            
Nazar = User(username='zoltraak', password='123456')
print(f"Имя: {Nazar.username}, Пароль: {Nazar.get_password()}")
new_password = input("Новый пароль: ")
Nazar.set_password(new_password)
print(f"Имя: {Nazar.username}, Новый пароль: {Nazar.get_password()}")
        
#1) _User__password
#2) _password python технически разрешает доступ (сделано для разработчиков), __password польностю блокирует доступ снаружи 