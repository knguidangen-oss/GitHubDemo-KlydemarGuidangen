#Blueprint
class Hero:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def take_damage(self, amount):
        self.hp = self.hp - amount
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0


#My characters
arthur = Hero("Arthur", 100, 15)
morgana = Hero("Morgana", 80, 20)

#Arthur takes damage
# Arthur takes 10 damage manually
arthur.take_damage(10)

print("--- Initial Damage Check ---")
print("Arthur takes damage")
print("Arthur HP:", arthur.hp)    # Health: 90
print("Morgana HP:", morgana.hp)  # Health: 80
print()


#Final Status
print("--- Final Status ---")
print("Arthur final health:", arthur.hp)
print("Is Arthur alive?", arthur.is_alive())
print("Morgana final health:", morgana.hp)
print("Is Morgana alive?", morgana.is_alive())
