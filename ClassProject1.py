import random
def game(comp,user_choice):
    if comp==user_choice:
        return None
    elif comp=="stone":
        if user_choice=="paper":
            return True
        elif user_choice=="scissor":
            return False
    elif comp=="paper":
        if user_choice=="scissor":
            return True
        elif user_choice=="stone":
            return False
    elif comp=="scissor":
        if user_choice=="stone":
            return True
        elif user_choice=="paper":
            return False
    else:
        str="Please enter among the given options{stone,paper,scissor}.\nYour input is invalid."
        return str
while True:
       name=input("Enter the player's name: ")
       print(f"Hello {name} :):):)")
       print("Winning Rules of the Rock paper scissor game as follows: \n"
          + "Rock vs paper->paper wins \n"
          + "Rock vs scissor->Rock wins \n"
          + "paper vs scissor->scissor wins \n")

       print(f"{name}'s turn: For stone---->(1)\npaper------>(2)\nscissor------(3)")
       user=int(input("Enter your choice: "))
       if(user==1 or user==2 or user==3):
          pass
       else:
          print("You have entered wrong choice.\nchoose among For stone---->(1)\npaper------>(2)\nscissor------(3)")
          break
       user_choice=""
       if(user==1):
           user_choice="stone"
       elif(user==2):
           user_choice="paper"
       elif(user==3):
           user_choice="scissor"
       print(f"{name} choose: {user_choice}")

       print("Computer turn: choose among stone,paper,scissor")


       computer_choice=random.randint(1,3)
       if(computer_choice==1):
          comp="stone"
       elif(computer_choice==2):
          comp="paper"
       elif(computer_choice==3):
          comp="scissor"

       print(f"Computer's choice: {comp}")

       result=game(comp,user_choice)
       if(result==None):
         print("Game ends in a tie.")
       elif(result==True):
         print(f"{name} Wins.")
       elif(result==False):
         print("Computer Wins.\nBetter luck next time.")

       print("Do you want to play again!!!(y/n)")
       play_again=input()
       if (play_again.lower()=="n"):
           print("Thank you for Playing.")
           break
       else:
           print("Here we go again!!!!")




