from string import digits
from random import randint


valid = False
names = ['Jack','John']
pencils_taken_possibilities = ['1','2','3']


def change_player(next):
    return 'John' if next == 'Jack' else 'Jack'

def check_pencils_number():
    global valid
    valid = False

    while not valid:
        valid = True
        pencils_number = input()

        if pencils_number == '0':
            print('The number of pencils should be positive')
            valid = False
            continue

        for char in pencils_number:    
            if char not in digits:
                print('The number of pencils should be numeric')
                valid = False
                break
    
    return pencils_number

def check_first_player():
    global valid
    valid = False

    while not valid:
        valid = True
        next_player = input()
        
        if next_player not in names:
            print('Choose between \'John\' and \'Jack\'')
            valid = False

    return next_player

def do_move(pencils_number):
    winning_move = (pencils_number - 1) % 4
    pencils_taken = winning_move if winning_move != 0 else randint(1, pencils_number % 4) 

    print(pencils_taken)
    return pencils_taken


def __main__():
    # checking if total amount of pencils is positive and a numeric character 
    print("How many pencils would you like to use?")
    pencils_number = int(check_pencils_number())


    # getting in input the player to start the game
    print("Who will be the first (John, Jack):")
    next_player = check_first_player()


    # game body    
    valid = False
    while pencils_number > 0:
        pencils_taken = 0
        print(pencils_number * '|')
        print(f'{next_player}\'s turn:')

        if next_player == 'Jack':
            pencils_taken = do_move(pencils_number)
        else:
            valid = False
            while not valid:       # checking input integrity
                valid = True
                pencils_taken = input()
    
                if valid and (pencils_taken not in pencils_taken_possibilities):
                    print("Possible values: '1', '2' or '3'")
                    valid = False
                    continue
                
                if valid and (pencils_number < int(pencils_taken)):
                    print('Too many pencils were taken')
                    valid = False
                    continue
            
        next_player = change_player(next_player)
        pencils_number -= int(pencils_taken)
    
    print(f'{next_player} won!')



__main__()

    
