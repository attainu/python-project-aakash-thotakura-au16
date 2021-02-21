import random


class Dice:

    def rollDice():
        inp = input("Roll Dice: Press 'R' & then 'Enter'")
        if inp == 'r' or 'R':
            dice = random.randint(1, 6)
            return dice
