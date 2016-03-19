# Week 7, Chapters 1-6, Extra Credit, Part 2, Problem 2
# Calculate amount of financial assistance
# By: Brendan Albert

# Declare computeAssistance function header, the user's income and number of children are passed in as arguments
def computeAssistance(income, children):

    # If the user entered an income between 30,000 and 40,000, inclusive, and they have at least 3 children, they can receive $1,000 per child.
    if 30000 <= income <= 40000 and children >= 3:
        assistance = 1000 * children
    # If their income is between 20,000 and 30,000 and they have 2 or more children, they are eligible for $1,500 per child.
    elif 20000 <= income <= 30000 and children >= 2:
        assistance = 1500 * children
    # If their income is less than $20,000, they are eligible to receive $2,000 per child.
    elif income < 20000:
        assistance = 2000 * children
    # Otherwise, the user's income or number of children makes them ineligible to receive assistance.
    else:
        # Zero is returned which will be checked for in main to inform the user they are ineligible.
        return 0
    # The else was skipped so the user is likely eligible to receive assistance, which is passed to the calling function.
    return assistance

# Declare main function header
# Main has a while loop which prompts the user for the income and children inputs and returns the amount of assistance they are eligible to receive.
def main():
    # Prime the while loop by setting income to zero
    income = 0
    # While loop will continue prompting for inputs and returning the amount of assistance the user is eligible for, granted their income is positive.
    # -1 or any negative number serves as a sentinel value.
    while income >= 0:
        income = int(input("Please enter annual income (-1 to quit): "))
        # Check to be sure income is positive, otherwise the sentinel was entered indicating they would like to quit.
        # If income is positive then we enter and prompt for number of children.
        if income >= 0:
            children = int(input("Please enter number of children: "))
            # Pass user's inputs to function.  The returned assistance amount determines which statement is printed.
            if computeAssistance(income, children) > 0:
                print("Based on your provided information, you are eligible to receive ${:,.2f}".format(computeAssistance(income, children)))
            else:
                print("Based on your provided information, you are ineligible to receive assistance")
        else:
            print("Goodbye!")
# Call main as our program's entry point.
main()
            
