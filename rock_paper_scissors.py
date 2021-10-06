import random



def who_wins(user, computer):
    winner = 0
    if computer == 3:
        if user == 3:
            print("Its a tie!")
        elif user == 2:
            print("The computer wins!")



def main():
    computer = random.randrange(1, 4)
    user = int(input("Please enter a number 1-3 "))
    who_wins(user, computer)


if __name__ == '__main__':
    main()