import random



def generating_numbers(maximum, minimum):
    """

    :param maximum: is the maximum number up to 20
    :param minimum: is the minimum number at minimum 1
    :return: returns the number
    """
    if maximum >= 20:
        maximum = 20
    elif minimum <= 5:
        minimum = 5
    num1 = random.randint(minimum, maximum)
    return num1

def get_max():
    maximum = int(input("Pleas enter the maximum number for the equation "))
    minimum = int(input("Please enter the minimum number for the equation"))
    if maximum >= 20:
        maximum = 20
    else:
        return


def get_min():



def get_sign():
    """

    :return: returns the sign of the equation
    """
    x = input("Please enter the sign ")

    if x == "*":
        return "*"
    elif x == "-":
        return "-"
    else:
        return "+"

def getting_sign(sign, num1, num2):
    """

    :param sign: the sign of the equation
    :param num1: The first number of the equation
    :param num2: The second number of the equation
    """
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





def main():
    minimum =
    sign = get_sign()
    num1 = generating_numbers(minimum, maximum)
    num2 = generating_numbers(minimum, maximum)
    getting_sign(sign, num1, num2)

