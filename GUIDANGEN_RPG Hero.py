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


arthur = Hero("Arthur", 100, 15)
lancelot = Hero("Lancelot", 100, 10)
morgana = Hero("Morgana", 80, 20)

arthur.take_damage(10)
print("Arthur HP:", arthur.hp)
print("Morgana HP:", morgana.hp)
print()

arthur.take_damage(lancelot.attack)
print("Arthur health after Lancelot hit:", arthur.hp)
print("Is Arthur alive?", arthur.is_alive())
print()

for i in range(7):
    lancelot.take_damage(arthur.attack)
    print("Lancelot health after attack:", lancelot.hp)

print()
print("Lancelot final health:", lancelot.hp)
print("Is Lancelot alive?", lancelot.is_alive())
