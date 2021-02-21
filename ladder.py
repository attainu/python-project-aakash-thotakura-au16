from constants import *
import constants


class Ladder:

    def ladderMovement():
        if constants.position in ladder:
            print ('Congrats, You found a Ladder at position',
                   constants.position)
            constants.position = constants.position \
                + ladder[constants.position]

            print ('You are at: ', constants.position)
