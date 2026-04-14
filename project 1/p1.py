import random

# Print multiline instruction
print("Winning rules of the game ROCK PAPER SCISSORS are:\n"
      +"Rock vs Paper--> Paper win \n"
      +"Rock vs Scissors --> Rock win \n"
      +"Paper vs Scissors-->Scissors wins \n")
while True:
    print("Enter your choice \n 1 - Rock \n 2 -Paper \n 3 - Scissors \n")

    # Take the input from user
    choice=int(input("Enter your choice: "))

    # Looping until user enters valid input
    while choice > 3 or choice < 1:
        choice=int(input("Enter a valid choice please :"))

    # Initialize value of choice_name variable corresponding to the chocie value
    if choice==1:
        choice_name="Rock"
    elif choice==2:
        choice_name="Paper"
    else:
        choice_name="Scissor"
    
    # Pint user choice
    print("User chocie is:",choice_name)
    print("Now it's computer turn......")

    # conputer choose randomly any number among 1, 2, and 3
    comp_choice=random.randint(1,3)

    # Initialize value of comp_choice_name variable corresponding to the choice value
    if comp_choice==1:
        comp_choice_name='Rock'
    elif comp_choice==2:
        comp_choice_name='Paper'
    else:
        comp_choice_name='Scissors'
    print("Computer chpice is:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    # Determain the winner
    if choice==comp_choice:
        result="Draw"
    elif(choice==1 and comp_choice==2)or (comp_choice==1 and choice==2):
        result='Paper'
    elif(choice==1 and comp_choice==3)or (comp_choice==1 and choice==3):
        result='Rock'
    elif(choice==2 and comp_choice==3)or (comp_choice==2 and choice==3):
        result='Scissors'


    # Print the result
    if result=="Draw":
        print("<== it's a tie ==>")
    elif result==choice_name:
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")
    
    # Ask if the user wants to play again
    print("DO you want to play again (Y/N)")
    ans=input().lower()
    if ans=='n':
        break

# after coming out of the while loop print thanks for playing
print("Thanks for playing!!!")

