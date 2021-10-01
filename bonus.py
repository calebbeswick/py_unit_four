


def salary(years_worked, current_salary):
    if years_worked >= 5:
        total_salary = current_salary * 1.05
        print("Your total salary is ", total_salary)
    else:
        print("Your total salary is ", current_salary)

def main():
    years_worked = int(input("How many years have you worked at this company? "))
    current_salary = int(input("What is your current salary"))
    salary(years_worked, current_salary)


main()