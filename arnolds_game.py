import os
import random
import time


class LiveSoul:
    def __init__(self, name, hp: float, intellect: float, power: float, agility: float):
        self.name = name
        self.hp = hp
        self.intellect = intellect
        self.power = power
        self.agility = agility

        self.punch = self.get_punch_power()
        self.protection = self.get_protection_count()


    def __str__(self):
        return f"""
Имя: {self.name}.
Здоровье: {int(self.hp)}.

Сила: {self.power};
Интеллект: {self.intellect};
Ловкость: {self.agility};
"""

    def change_parameter(self):
        """ Изменение параметров персонажа в связи с баффами, или дебафами """

        types = ["Влияние на силу", "Влияние на интеллект", "Влияние на ловкость", "Влияние на количество жизненной энергии", "Нет влияния", "Влияние на силу удара"]
        type_of_fluence = types[random.randint(0, len(types) - 1)]
        print(type_of_fluence)


        match type_of_fluence:
            case "Влияние на силу":
                self.power += random.randint(-3, 7)
                print(self.power)
                return self.power

            case "Влияние на интеллект":
                self.intellect += random.randint(-3, 7)
                print(self.intellect)
                return self.intellect

            case "Влияние на ловкость":
                self.agility += random.randint(-3, 7)
                print(self.agility)
                return self.agility

            case "Влияние на количество жизненной энергии":
                self.hp += random.randint(-3, 7)
                print(self.hp)
                return self.hp

            case "Нет влияния":
                pass

            case "Влияние на силу удара":
                self.punch += random.randint(-3, 7)
                print(self.punch)
                return self.punch


    def get_punch_power(self):
        """ Определяем силу удара персонажа """

        punch = self.power * 0.1 + self.intellect * 0.08 + self.agility * 0.1
        creet = random.randint(0, 10)
        if creet == 0:
            print(f"!!! Крит !!!")
            return punch * 5
        return punch * 2


    def get_protection_count(self):
        """ Определяем коэффициент защиты персонажа """

        return self.power * 0.1 + self.intellect * 0.05 + self.agility * 0.05


    def take_punch(self, enemys_punch):
        """ Вычисление принятого урона """

        hp = enemys_punch * self.protection
        self.hp -= hp
        return self.hp


def fight_results(my_character: LiveSoul, monster: LiveSoul):
    """ Результаты боя нашего персонажа и монстра """

    my_prev_hp = my_character.hp
    monster_prev_hp = monster.hp

    monsters_punch = monster.get_punch_power()
    my_character.hp = my_character.take_punch(monsters_punch)
    print(f"Монстр ударил {monster.punch}, и снес мне {int(-my_character.hp + my_prev_hp)} очков жизненной энергии")

    my_punch = my_character.get_punch_power()
    monster.hp = monster.take_punch(my_punch)
    print(f"Я ударил монстра на {my_punch}, и снес ему {int(-monster.hp + monster_prev_hp)} очков жизненной энергии")


os.system("cls")
monsters = ["Zombie", "Spider", "Creeper", "Wolf", "Wild-Leon", "Wild Bird"]

characters_name = input("Введите имя персонажа: ")
my_character = LiveSoul(characters_name, 50, 5, 5, 5)
print(my_character)

cycle_1 = cycle_2 = True

while cycle_1:
    os.system("cls")

    monster = LiveSoul(
        name=monsters[random.randint(0, len(monsters) - 1)],
        hp=random.randint(10, 50),
        intellect=random.randint(1, 10),
        power=random.randint(1, 10),
        agility=random.randint(1, 10)
        )
    print(monster)

    while cycle_2:
        os.system("cls")

        fight_results(my_character, monster)
        print(monster)
        my_character.change_parameter()
        print(my_character)
        time.sleep(3)

        if int(my_character.hp) <= 0:
            print(f"{monster.name} оказался сильнее!")
            cycle_1 = False
            cycle_2 = False

        elif int(monster.hp) <= 0:
            print(f"Я оказался сильнее {monster.name}")
            cycle_2 = False

        else:
            continue

    cycle_2 = True
    next_game = input("Еще кон?: ")
    if next_game != "":
        cycle_1 = False



