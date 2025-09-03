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
    
    def receive_attack(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0

    def attack(self, target):
        damage = self.__level * 2
        target.receive_attack(damage)
        print(f"{self.get_name()} atacou {target.get_name()} e causou {damage} de dano!")

class Hero(Character):
    def __init__(self, name, life, level, skill):
        super().__init__(name, life, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill
    
    def display_details(self):
        return f"{super().display_details()}\nHabilidade: {self.get_skill()}\n"
    
    def special_attack(self, target):
        damage = self.get_level() * 5
        target.receive_attack(damage)
        print(f"{self.get_name()} usou a habilidade especial {self.get_skill()} em {target.get_name()} e causou {damage} de dano!")
    
class Enemy(Character):
    def __init__(self, name, life, level, type):
        super().__init__(name, life, level)
        self.__type = type
    
    def get_type(self):
        return self.__type
    
    def display_details(self):
        return f"{super().display_details()}\nTipo: {self.get_type()}\n"
    
class Game:
    def __init__(self) -> None:
        self.hero = Hero(name="Herói", life=100, level=5, skill="Super Força")
        self.enemy = Enemy(name="Morcego", life=50, level=3, type="Voador")

    def start_battle(self):
        print("Iniciando batalha!")
        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("\nDetalhes dos Personagens:")
            print(self.hero.display_details())
            print(self.enemy.display_details())

            input("Pressione Enter para atacar...")
            choice = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

            if choice == "1":
                self.hero.attack(self.enemy)
            elif choice == "2":
                self.hero.special_attack(self.enemy)
            else:
                print("Escolha inválida. Escolha novamente.")

            if self.enemy.get_life() > 0:
                self.enemy.attack(self.hero)
        
        if self.hero.get_life() > 0:
            print("\nParabéns, você venceu a batalha!")
        else:
            print("\nVocê foi derrotado!")
    
game = Game()
game.start_battle()
