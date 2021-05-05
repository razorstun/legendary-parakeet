from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''

    while guess not in ['0','1','2']:
        guess = input("Pick a number:  0,1 or 2: " )

    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct")
    else:
        print("Wrong guess!")
        print(mylist)


mylist = ['O','','']

mixedup_list = shuffle_list(mylist)

guess = player_guess()

check_guess(mixedup_list,guess)