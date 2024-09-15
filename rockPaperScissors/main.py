import random
'''
1 for rock
-1 for paper
0 for scissors 
'''
def game():
    computer = random.choice([-1,0,1])
    you = input("Enter your choice:\nr for Rock\np for Paper\ns for Scissors\n")
    if you not in ["r", "p", "s"]:
        print("Invalid input. Please try again.")
        
    else:
        dic = {"r":1 ,"p":-1, "s":0}
        choice = dic[you]
        reverseDic = {1:"Rock", -1:"Paper", 0:"Scissors"}
        print(f"You choose {reverseDic[choice]} and Computer choose {reverseDic[computer]}")
        if(computer == choice):
            print("It's a tie!")
        else:
            if(computer == -1 and choice == 1):
                print("You Lose!")
            elif(computer == -1 and choice == 0):
                print("You Win!")
            elif(computer == 1 and choice == -1):
                print("You Win!")
            elif(computer == 1 and choice == 0):
                print("You Lose!")
            elif(computer == 0 and choice == 1):
                print("You Win!")
            elif(computer == 0 and choice == -1):
                print("You lose!")
            else:
                print("Something went wrong")

while True:
    game()
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break