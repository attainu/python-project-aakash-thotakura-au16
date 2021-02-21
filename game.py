from player_movement import Movement
import constants

print("Press 's' to start")
inp = input('')
if inp == 's':


    def game():
        name = input('Enter Your Name: ')
        player_movement = Movement.playerMovement()
        print ('CONGRATUATIONS!!!', name, 'has WON')

        constants.position = 1
        print('Do you want to re-try?')
        enter = input('y/n')
        if enter == 'y':
            game()
        else:
            print('bye')
