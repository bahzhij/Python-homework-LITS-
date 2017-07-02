import itertools
import random
import time
import datetime
now = datetime.datetime.now()
prompt = "> "


def start():

    lobby()

def game_over(text):

    print(text)
    print("Do you want to play again? (y / n)")

    choice = ""
    while choice != "y" and choice != "n":
        choice = input("> ")
        if choice == "y":
            start()
        elif choice == "n":
            exit(0)

def room_1(name):
	
	print("Hello {0}, we're going to walk through the rooms and play some cool games.\nIf you win - you go to the next room.\nI hope you would get to the last room.\n Good luck!".format(name))
	time.sleep(10)
	print('............')
	print("{0}, to enter the house you need to open the lock.\nThe lock code has 3 digits and you have 20 tries to guess it.".format(name))

	player_attempts = 0
	code = random.randint(000, 999)
	while player_attempts < 20:
	    print()
	    guess = int(input(prompt))
	    
	    player_attempts =+ 1
	    
	    if guess < code:
	        print('\nWRONG  - code is too low')
	        
	    if guess > code:
	        print('\nWRONG  - code is too high')
	        
	    if guess == code:
	        break
	        
	if guess == code:
	    player_attempts = str(player_attempts)
	    print('\nverifying ....')
	    time.sleep(2)
	    print('\nСongratulations! Door is open')
	    room_2()
	    
	if guess != code:
	    code = str(code)
	    print('\n....')
	    time.sleep(1)
	    print('\n....')
	    time.sleep(1)
	    game_over('\nGAME OVER  - the code was ' + code)
	    
def room_2():

	print('............')
	print("Now, {0}, you're in the house. To enter the first room, please do a simple calculation:\nImagine you were born in 1937.\nHow many years is the difference between your imaginable and real age?".format(name))
	years_difference = int(input(prompt))
	def count_years(years_difference):
		diff = now.year - 1937 - age

		if years_difference == diff:
			print("You're right! Welcome to the next room")

		else:
			game_over("GAME OVER\nSorry, it was so simple... The difference is {0} years".format(diff))
			
	count_years(years_difference)

def room_3():
	print("Room 3")

def lobby():

    print("I'd like to ask you a few questions before we start.\nWhat is your name?")
    playerName = input(prompt)
    print("How old are you?")
    playerAge = int(input(prompt))
    print("Where do you live?")
    playerCity = input(prompt)

    return (playerName, playerAge, playerCity)

name, age, city = lobby()
room_1(name)





start()