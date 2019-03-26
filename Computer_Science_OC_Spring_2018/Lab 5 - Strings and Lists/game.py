# Author: Trevor Martin
# Date of Completion: 16 March 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 5, game.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# The game Mastermind
#===================================================================================================
# DEPENDENCIES
#===================================================================================================
import random
#===================================================================================================

print('{}\n{}\n{}\n{}'.format("Guess the four color code.","There are R,G,O,B,Y, and P.",
                          "Black pegs mean correct color in correct position.",
                          "White pegs mean correct color in but in the wrong position.",
                          "A color and position cannot be both a white_pegs and black_pegs peg."))

# choose random index for color list four times
def generate_hidden_code():
    colors = ["R","G","O","B","Y","P"]
    hidden_code = ""
    for color in range(4):
        random_number = random.randint(0,5)
        color = colors[random_number]
        hidden_code += color
    return hidden_code

# play Mastermind
def Mastermind(hidden_color_code):
    NUM_TURNS=0
    done = False
    while not done and NUM_TURNS < 10:
        black_pegs = 0
        white_pegs = 0
        user_guess=input(str("What's your user_guess: "))
        new_user_guess = user_guess
        new_hidden_color_code = hidden_color_code
        if new_user_guess == hidden_color_code:
            print("You got it friend")
            done=True
        else:
            NUM_TURNS += 1
            current_turns = 10 - NUM_TURNS
            for i in range(len(new_user_guess)):
                if new_user_guess[i]==new_hidden_color_code[i]:
                    black_pegs+=1
                    new_user_guess=new_user_guess[0:i]+" "+new_user_guess[i+1:]

                    new_hidden_color_code = new_hidden_color_code[0:i]+"W"+new_hidden_color_code[i+1:]
                    
            for i in range(len(new_user_guess)):
                for j in range(len(new_user_guess)):
                    if new_user_guess[j] !=" " and new_user_guess[j] == new_hidden_color_code[i]:
                        white_pegs += 1
                        new_user_guess=new_user_guess[0:j]+"Y"+new_user_guess[j+1:]
                        new_hidden_color_code=new_hidden_color_code[0:i]+"Z"+new_hidden_color_code[i+1:]
        print('{}{}{}\n{}{}{}{}{}{}{}{}'.format("This guess: ",user_guess,"is wrong. ","You have ",current_turns," turns left ",
                                   "and have ",black_pegs," black pegs and ",white_pegs," white pegs."))

        white_pegs=0
        black_pegs=0
def main():
    hidden_color_code = generate_hidden_code()
    Mastermind(hidden_color_code)

main()


    












