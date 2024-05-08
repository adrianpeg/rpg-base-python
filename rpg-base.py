import random

stage = 0


def enemy():
    enemy_type = random.randint(1, 3)

    if enemy_type == 1:
        enemy_name = "goblin"
        enemy_hp = 30
        enemy_att = 2
        enemy_def = 4
        enemy_int = 4
    elif enemy_type == 2:
        enemy_name = "orc"
        enemy_hp = 40
        enemy_att = 4
        enemy_def = 6
        enemy_int = 0
    else:
        enemy_name = "elf"
        enemy_hp = 20
        enemy_att = 4
        enemy_def = 2
        enemy_int = 4
    return enemy_name, enemy_hp, enemy_att, enemy_def, enemy_int


enemy_name, enemy_hp, enemy_att, enemy_def, enemy_int = enemy()

print("Welcome to the world of simple base RPG")
input("Press enter to continue")
elect = input("""Choose a character to start:

1. Warrior.
2. Mage.
3. Archer.
4. Cleric.
5. Tank.

""")

while elect not in ["1", "2", "3", "4", "5"]:
    elect = input("You haven't chosen a valid character, please try again: ")

if elect == "1":
    pj_name = "warrior"
    pj_hp = 100
    pj_att = 5
    pj_def = 4
    pj_int = 1
elif elect == "2":
    pj_name = "mage"
    pj_hp = 90
    pj_att = 2
    pj_def = 1
    pj_int = 7
elif elect == "3":
    pj_name = "archer"
    pj_hp = 90
    pj_att = 7
    pj_def = 2
    pj_int = 1
elif elect == "4":
    pj_name = "cleric"
    pj_hp = 100
    pj_att = 3
    pj_def = 3
    pj_int = 4
elif elect == "5":
    pj_name = "tank"
    pj_hp = 150
    pj_att = 1
    pj_def = 5
    pj_int = 3

print(f"Now you are an amazing {pj_name}")
print(f"Your HP is {pj_hp}")
print(f"Your attack is {pj_att}")
print(f"Your defense is {pj_def}")
print(f"Your intelligence is {pj_int}")

while stage != 10:
    stage += 1
    print(f"Stage {stage}")
    input("Press enter to continue\n")
    print(f"A {enemy_name} has appeared")
    print(f"His base HP is {enemy_hp}")
    print(f"His base attack is {enemy_att}")
    print(f"His base defense is {enemy_def}")
    print(f"His base intelligence is {enemy_int}")

    while pj_hp > 0 and enemy_hp > 0:
        combat = input("""Decide what to do:

1. Attack.
2. Defense.
3. Cast Spell.
4. Check my stats.

""")
        if combat == "1":
            luck = random.randint(1, 10)
            final_hit = pj_att + luck
            print(f"Your attack of {pj_att} plus a roll of {luck} results in {final_hit} points of damage")
            effect = final_hit - enemy_def
            if effect > 0:
                enemy_hp -= effect
                print(f"You have attacked {enemy_name} with {effect} damage")
                print(f"Now his HP is {enemy_hp}")
                if enemy_hp <= 0:
                    print(f"You have defeated {enemy_name}!")
                    enemy_name, enemy_hp, enemy_att, enemy_def, enemy_int = enemy()
                    break
            else:
                print(f"You have missed the attack on {enemy_name}")
            effect = enemy_att - pj_def
            if effect > 0:
                pj_hp -= effect
                print(f"You have been attacked by {enemy_name} with {effect} damage")
                print(f"Now your HP is {pj_hp}")
                if pj_hp <= 0:
                    print("You have died!")
                    exit()
            else:
                print(f"The {enemy_name} has missed the hit.")
        elif combat == "2":
            pj_hp += 3
            pj_def += 2
            print("You have healed yourself 3 hp points and have increased your defense in 2 points")
        elif combat == "3":
            spell = input("""Choose which spell to use:      
1. Fireball
2. Buff
3. Heal
""")
            if spell == "1":
                cast = pj_int + 5
                enemy_hp -= cast
                print(f"You have dealt {cast} points of damage to the enemy")
            elif spell == "2":
                cast = pj_int + 5
                pj_att += cast
                print(f"Your attack has been increased by {cast}")
            elif spell == "3":
                cast = pj_int + 5
                pj_hp += cast
                print(f"You have healed yourself {cast} points of life")
            else:
                print("You have failed the spell")

        elif combat == "4":
            print(f"Your HP is {pj_hp}")
            print(f"Your attack is {pj_att}")
            print(f"Your defense is {pj_def}")
            print(f"Your intelligence is {pj_int}")
            input("Press enter to continue")
        else:
            print("You have not chosen a valid option")

    if stage == 10:
        print("You won!")
        break
