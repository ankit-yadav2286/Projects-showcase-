import random
random_number=random.randint(1,100)
print('''GAME RULES: You have to guess a number between 1 to 100.
if your guess is same as that of the randomly choose number you win.
''')
guesses=0
number=None
while(number != random_number):
    number = int(input("Enter the number between 1 to 100: "))
    if(number>100):
        print("Invalid input!!1\nPlease enter the number between 1 and 100 only.")
        break
    guesses+=1
    if(number==random_number):
        print(f"You have guessed the right number {number}")

    elif(number<random_number):
        print("You guessed the wrong number!Enter the higher number.")
    elif(number>random_number):
        print("You guessed the wrong number!Enter the lower number. ")

print(f"The number of guesses you took is {guesses}")

with open("hiscore1.txt","r") as f:
    prev_hi_score=f.read()
if(guesses>int(prev_hi_score)):
    with open("hiscore1.txt","w") as f:
        f.write(f"{guesses}")

