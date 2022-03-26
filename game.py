import random
def luck_num(h):
    g = 0
    if h == 2:
        g = 10
    if h == 3: g = 100
    if h == 4: g = 1000
    ram = '1234567890'
    lucky_number = "".join(random.sample(ram, h))
    lucky_number = int(lucky_number)
    lucky_numbers = str(lucky_number)
    print(lucky_number)
    print("Your number is between ", int(lucky_numbers)-int(lucky_numbers[1:]),"and",(int(lucky_numbers)+g)-int(lucky_numbers[1:]))
    return lucky_number


speech = ["Ops, You miss it.\U0001F604", 
"You miss it again.", 
"Try again. \U0001F618 You can guess it."]
def guess(lucky_number):
    chance = 3
    have_chance = True
    print("We gave you three chaces to guess the lucky number if you don't catch the lucky number within 3 chances, You will Lose!")
    print("Good Luck!")

    while have_chance == True:
        guess = input("Guess Lucky number: ")
        try:
            guess = int(guess)
        except:
            print("It isn't a number. Try Numbers.")
            continue
        if guess == lucky_number:
            print("You Win!\U0001F600")
            print("Hooray!")
            break
        elif chance > 1:
                if lucky_number - guess <= 3:
                    print("Too Close, Keep trying!")
                else:
                    print(random.sample(speech, 1))
                print("You have " + str(chance -1 ) + "chance !")
        chance -= 1
        if chance == 0:
            print("Opps,You Lose!")
            have_chance = False


def easy():
    print("You have to guess 2-digits lucky number to win.")
    guess(luck_num(2))

def med():
    print("You have to guess 3-digits lucky number to win.")
    guess(luck_num(3))

def diff():
    print("You have to guess 4-ditgits lucky number to win.")
    guess(luck_num(4))
mode = input("""Choose your mode:   esay?
                    medium?
                    hard?
Your ans: """)
if mode == "easy": easy()
elif mode == "medium": med()
elif mode == "hard": diff()
else: print("Spelling Incorrect")