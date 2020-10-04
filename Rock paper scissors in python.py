#This code is taken form  :   https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/



from random import randint          # From random module is randint is imported because it give random value in integer with a specific range 

t=['rock','paper','scissor']         # list of play option

computer = t[randint(0,2)]          # assign a random play to the computer Why (0,2)? Remember that computers start counting at 0.

player = False                      # set the player to False









while player == False:                           # while loop is use it compare the give statement if it fullfil the requirment it will print the assign message 
    player = input("rock, paper scissors ?: ")
    if player == computer:
        print('Tie')
    elif player == 'rock':                                    # for rock 
        if computer == 'paper':
            print('you lose',computer, 'covers',player)
        else:
            print('you win ',player,'smashes',computer)
    elif player == 'paper':                                 # for paper
        if computer == 'scissors':
            print('you lose',computer, 'cut',player)
        else:
            print('you win ',player,'cover',computer)

    elif player == 'scissors':                             # for scissor 
        if computer == 'rock':
            print('you lose',computer, 'smashes',player)
        else:
            print('you win ',player,'cut',computer)
    else:
        print('this is not valid play check your spelling')      # if the user enter wrong spelling 



        
    player = False                             #player was set to True, but we want it to be False so that loop continues
    computer  = t[randint(0,2)]




        
