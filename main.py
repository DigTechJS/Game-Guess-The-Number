# Guess the number
import random
randomNo=random.randint(1,100)
# print(randomNo)
print("Get ready for an amazing game--> Guessing the number")
userGuess=int(input("Enter your number between 1 and 100:\n"))
guesses=1

while (userGuess!=randomNo):
    if userGuess==randomNo:
        print("You guessed it right!")
        print("*************************************************")
    elif userGuess>randomNo:
        print("You guessed it Wrong!")
        print("Lower Number please")
        print("*************************************************")
    else:
        print("You guessed it Wrong!")
        print("Higher number please")
        print("*************************************************")
    guesses+=1
    userGuess=int(input("Enter again:\n"))
print(f'''Congratulations!!!
You guessed it in: {guesses} guesses''') 
with open("hiscore.txt","r") as f:
    hiscore=int(f.read())
    
    if guesses<hiscore:
        print('''Congratulations!!!
        You have just broke the highscore''')
        with open("hiscore.txt",'w') as f:
            f.write(str(guesses))
        