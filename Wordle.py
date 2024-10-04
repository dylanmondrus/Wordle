#Tulane University, CMPS 1500, Spring 2024
#
#
#Student name: Dylan Mondrus
#Student email address: dmondrus@tulane.edu
#

import random

from WordleWordlist import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def enter_action(guessedword):
    """ This function is called any time the enter button
    is clicked/typed in the game. guessedword is the player's most
    recent guess which needs to be checked.
    """
    guessedword = guessedword.lower()


    if guessedword in FIVE_LETTER_WORDS: #check if user word is in word list
        for i, letter in enumerate(guessedword): #get index and value of user word
            if letter == solution[i]: #check for green key
                gw.set_square_color(gw.get_current_row(),i,CORRECT_COLOR)
                gw.set_key_color(letter.upper(), CORRECT_COLOR)#set the color of the key
            elif letter in solution and letter != solution[i]:#check for yellow key
                gw.set_square_color(gw.get_current_row(),i,PRESENT_COLOR)
                if gw.get_key_color(letter.upper()) != CORRECT_COLOR:
                    gw.set_key_color(letter.upper(), PRESENT_COLOR)
            else:
                gw.set_square_color(gw.get_current_row(),i,MISSING_COLOR)#check for gray key
                gw.set_key_color(letter.upper(),MISSING_COLOR)

        if guessedword != solution:#move on to next row
            gw.set_current_row(gw.get_current_row()+1)
        else:
            gw.show_message("You win!")




    else:
        gw.show_message("Not in word list")




solution = random.choice(FIVE_LETTER_WORDS)
print(solution)


gw = WordleGWindow()
gw.add_enter_listener(enter_action)





