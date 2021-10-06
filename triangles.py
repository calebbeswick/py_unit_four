
def is_triangle(side1, side2, side3):
    if side1 >= (side2 + side3) or side2 >= (side1 + side3) or side3 >= (side1 + side2):
        return True
    else:
        return False




def main():
    pass

   # is_triangle(side1, side2, side3)



if __name__ == '__main__':
    main()

