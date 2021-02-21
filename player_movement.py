from dice import Dice
from ladder import Ladder
from snake import Snake
from constants import *
import constants
import sys
from design import Pattern


class Movement:

    def playerMovement():
        name = input('Enter Your Name: ')

        while True:

            dice_value = Dice.rollDice()

            if constants.position + dice_value == target:

                print ('dice_value value:', dice_value, 'You are at 100'
                       )
                print ('***You WIN***')
                dsgn = Pattern.vicdesig()
                print ('CONGRATUATIONS!!!', name, 'has WON')
                break
            
            elif constants.position + dice_value > target:

                print ('dice_value value:', dice_value, 'You are at: ',
                       constants.position)
                print ('Position Beyond 100, RE-PLAY')
                print ('Needed', target - constants.position)
                
            elif constants.position + dice_value < target:

                constants.position = constants.position + dice_value
                print ('dice_value value:', dice_value, 'You are at: ',
                       constants.position)
                ladder_value = Ladder.ladderMovement()
                snake_value = Snake.snakeMovement()
