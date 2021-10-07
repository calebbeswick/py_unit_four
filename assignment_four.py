import random






def generating_numbers():
    maximum = int(input("Please enter the maximum number of the equation "))
    minimum = int(input("Please enter the minimum number of the equation "))
    sign = input("Please enter the sign of the question. (+, *, or -) ")
    if maximum >= 20:
        maximum = 20
    elif minimum <= 1:
        minimum = 1
    num1 = random.randint(minimum, maximum)
    num2 = random.randint(minimum, maximum)
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




generating_numbers()



