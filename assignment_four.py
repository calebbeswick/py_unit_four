import random






def generating_numbers(maximum, minimum):
    if maximum >= 20:
        maximum = 20
    elif minimum <= 1:
        minimum = 1
    num1 = random.randint(minimum, maximum)
    return num1


def get_sign():
    x = input("Please enter the sign ")

    if x == "*":
        return "*"
    elif x == "-":
        return "-"
    else:
        return "+"

def getting_sign(sign, num1, num2):
    if sign == "*":
        question = num1 * num2
        print(num1, "*", num2)
    elif sign == "-":
        question = num1 - num2
        print(num1, "-", num2)

    else:
        question = num1 + num2
        print(num1, "+", num2)


    answer = int(input("What is the answer? "))
    if answer == question:
        print("You got it right!")
    else:
        print("You are incorrect")
    return sign




def main():
    maximum = int(input("Please enter the maximum number of the equation "))
    minimum = int(input("Please enter the minimum number of the equation "))
    sign = get_sign()
    num1 = generating_numbers(minimum, maximum)
    num2 = generating_numbers(minimum, maximum)
    getting_sign(sign, num1, num2)

