import random

def checkForDuplicates(number):
    if(len(set(number)) == 4):
        return True
    else:
        return False
    
while True:
    number = random.randint(1000,9999)
    computer_generated = [i for i in str(number)]
    if(checkForDuplicates(computer_generated)):
        break
    
print("\nComuter has generated a random 4 digit number which does not start from zero! Start Guessing!!")
trials = 0
while True:
    cows = 0
    bulls = 0
    user = input("\nEnter your 4-digit number: ")
    user_input = [i for i in user]
    if (user_input[0]=='0'):
        print("\n Sorry. your number cannot start with zero")
    elif (len(user_input) !=len(computer_generated)):
        print(f"\n Please enter {len(computer_generated)}-digit number ")
    elif(not checkForDuplicates(user_input)):
        print("\n please enter a number without repeating the digits.")
    else:
        for i in range (len(computer_generated)):
            if (computer_generated[i] == user_input[i]):
                cows = cows + 1
            elif(user_input[i] in computer_generated):
                bulls = bulls + 1
        trials = trials + 1
        if int(user) == number:
            print(f"\n Congrats you Guessed the correct number in {trials} trials. Well done :)")
            break
        else:
            print(f"\n Sorry you didn't guess the correct number! Cows = {cows}, Bulls = {bulls}")
            
            
