import random



def who_wins(user, computer):
    if computer == 3:
        if user == 3:
            print("Its a tie!")
        elif user == 2:
            print("The computer wins!")
        elif user == 1:
            print("The user wins!")
    if computer == 2:
        if user == 2:
            print("Its a tie!")
        elif user == 1:
            print("The computer wins!")
        elif user == 3:
            print("The user wins!")
    if computer == 1:
        if user == 1:
            print("Its a tie!")
        elif user == 3:
            print("The computer wins!")
        elif user == 2:
            print("The user wins!")



def main():
    computer = random.randrange(1, 4)
    user = int(input("Please enter a number 1-3 "))
    who_wins(user, computer)


if __name__ == '__main__':
    main()