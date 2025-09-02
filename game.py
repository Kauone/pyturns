class Character: 
    def __init__(self, name, life, level):
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__name
    
    def get_life(self):
        return self.__life
    
    def get_level(self):
        return self.__level
    
    def display_details(self):
        return f"Nome: {self.get_name()}\nVida: {self.get_life()}\nNível: {self.get_level()}"
    
class Hero(Character):
    def __init__(self, name, life, level, skill):
        super().__init__(name, life, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill
    
    def display_details(self):
        return f"{super().display_details()}\nHabilidade: {self.get_skill()}\n"
    
class Enemy(Character):
    def __init__(self, name, life, level, type):
        super().__init__(name, life, level)
        self.__type = type
    
    def get_type(self):
        return self.__type
    
    def display_details(self):
        return f"{super().display_details()}\nTipo: {self.get_type()}\n"
    
hero = Hero(name="Herói", life=100, level=5, skill="Super Força")
print(hero.display_details()) 
enemy = Enemy(name="Morcego", life=50, level=3, type="Voador")
print(enemy.display_details())