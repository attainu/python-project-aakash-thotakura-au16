from constants import *
import constants


class Snake:

    def snakeMovement():
        if constants.position in snake:
            print ('Oops!, swallowed by SNAKE at position',
                   constants.position)
            constants.position = constants.position \
                - snake[constants.position]
            print ('You are at: ', constants.position)
