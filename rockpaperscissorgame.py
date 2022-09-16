import random

if __name__=='__main__':
    pass


def display():
    print(f"you chose {Taking_choice.user_action}, and computer chose {Taking_choice.comp_action}")

    
def Taking_choice():
    Taking_choice.user_action = input("Enter your choice:('rock','paper',scissor'): ")

    possible_action = ["rock","paper","scissor"]

    Taking_choice.comp_action = random.choice(possible_action)
    game()


    
def game():
    user_action = Taking_choice.user_action
    comp_action = Taking_choice.comp_action

    
    if user_action == comp_action:
        display()
        print("Its TIE!")
        

    elif user_action == 'rock':
        display()
        if comp_action == 'paper':
            print("you LOSE!")
            
        else :
            print("you WIN!")
            

    elif user_action == 'paper':
        display()
        if comp_action == 'scissor':
            print("you LOSE!")
            
        else:
            print("you WIN!")
            

    elif user_action == 'scissor':
        display()
        if comp_action == 'rock':
            print("you LOSE!")
            
        else:
            print("you WIN!")
            

    else:
        print("That's not valid play, check your spelling.")

        

        

    play_again = input("Want to play again? (y/n): ")
    
    if play_again in "nN":
        print("Bye Bye!")
        exit
    elif play_again in "yY":
        Taking_choice()
    else:
        print("INVALID CHOICE")
        




Taking_choice()


