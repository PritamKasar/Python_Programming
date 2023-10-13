import random

options = ["Rock", "Paper", "Scissors"]

choice_user = input("Choose Rock, Paper, or Scissors: ")
generated  = random.choice(options)
print("You chose: ", choice_user )
print("Computer chose: ", generated ) 

if choice_user  == generated :
    print("It's a tie!")
elif choice_user  == "Rock" and generated  == "Scissors":
    print("You win!")
elif choice_user  == "Paper" and generated  == "Rock":
    print("You win!")
elif choice_user  == "Scissors" and generated  == "Paper":
    print("You win!")
else:
    print("Computer wins!")
