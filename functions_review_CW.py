def main():
    # problem1()
    problem2()


# ### Problem 1:
# ##### We will keep having this problem until EVERYONE gets it right without help (with variations :-P )
# * Create a function that has a loop
# * Prompt for numbers until the user enters ```q``` to quit
# * If the user doesn't enter ```q```, ask them to input another number
# * When the user enters ```q``` to quit, print the SUM of all numbers entered
#
# BONUS:
# * Write your code so that it it doesn't matter if the User enters a lowercase or an uppercase ```q``` to quit
# * Add extra validation to check that if the User doesn't enter ```q``` what they did enter is actually a number

def problem1():
    ask = input("Enter a number. Press 'Q' to quit")
    numbers = []
    while (ask.lower() != 'q'):
        ask = input("Enter another number")
        if (ask.lower() == 'q'):
            print(sum(numbers))
        else:
            numbers.append(int(ask))
            continue

# ### Problem 2:
# * Create a function ```problem2()```
# * In this function prompt the user for 2 numbers
#     * Create a second function called ```do_the_math``` that accepts 2 parameters (the 2 entered numbers)
# * In the ```do_the_math``` calculate the SUM, DIFFERENCE, PRODUCT, and QUOTIENT (division result)
# and return them as a dictionary to the calling function
# Example: Dictionary result returned if the argumants ```25``` and ```10``` are passed to the function:
# ```{'diff': 15, 'prod': 250, 'quot': 2.5, 'sum': 35}```
# * In your ```problem2()``` function, print the dictionary result returned from
# your ```do_the_math``` function using string literal formatting
# Example: Execution and Output
# ```
# Enter the First Number in the calculation:
# 25
# Enter the Second Number in the calculation:
# 10
# Here are your results for the numbers 25 and 10:
#     The SUM result is 35
# The DIFFERENCE result is 15
# The PRODUCT result is 250
# The DIVISION result is 2.5
#
# ```

def problem2():
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter another number"))

    print(f"The results of {num1} and {num2} are:\n {do_the_math(num1, num2)}")

def do_the_math(num1, num2):
    sum = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    quot = num1 // num2

    equationList = [{
        'sum': sum,
        'diff': diff,
        'prod': prod,
        'quot': quot
    }]
    for eq in equationList:
        return(f"The Sum is: {eq['sum']}\nThe DIFFERENCE is: {eq['diff']}\nThe PRODUCT is: {eq['prod']}\nThe QUOTIENT is: {eq['quot']}")


if __name__ == '__main__':
    main()
