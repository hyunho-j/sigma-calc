"""
Do not use multiple variables
Run with python 3
"""

def explicitize_multiplication(formula):
    edited_formula = ""
    for i in range(0, len(formula)-1):
        edited_formula += formula[i]
        if formula[i].isnumeric():
            if formula[i+1].isalpha():
                edited_formula += '*'
    edited_formula += formula[-1]
    return edited_formula


def sigma(start, end, formula):
    formula = explicitize_multiplication(formula)
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
    formula = input("\nEnter the formula for the terms.\n\
Usable symbols are:\n+, -, *, /, ^, and (). \n\n\
Formula:\n")
    
    print("\ncalculating...\n")

    result = sigma(start, end, formula)
    if result > 1e10:
        print("{:e}".format(result))
    else:
        print(result)


if __name__ == "__main__":
    main()