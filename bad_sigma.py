import math

def sigma(start, end, formula):
    sum = 0
    for i in range(start, end+1):
        substituted = ""
        for char in formula:
            if char.isalpha():
                substituted += str(i)
            elif char == "^":
                substituted += "**"
            else:
                substituted += char

        sum += eval(substituted)

    
    return sum


def main():
    
    start = int(input("Enter the first value of n (n is the index of summation):\n"))
    end = int(input("\nEnter the last value of n:\n"))
    formula = input("\nEnter the formula for the terms with only one or zero variables.\n\n\
Usable symbols are:\n+, -, *, /, ^, and (). \n\n\
Note that all multiplications must be explicit, which means that expressions such as 3x or 3n must be written as 3*x or 3*n respectively.\n\n\
Formula:")
    
    print("\ncalculating...\n")

    result = sigma(start, end, formula)
    print(result)


if __name__ == "__main__":
    main()