# snake-and-ladder

Create a CLI tool that plays a single player game of snakes and ladder using Pythong 3.9.6. 

# Rules:

* You must continue to roll the dice till you reach position 100 exactly. You will start at position 1.
* If your new position after the roll is at snake[key], then you have landed on a snake and must move back snake[value] places.
* Similarly, if you have landed on a ladder[key], then you move up to the value of ladder[value].
* If your position is near the end of the game and you do not roll enough to move exactly to 100, you do not move forward and need to repeat until you get the right integer to reach your target(100).