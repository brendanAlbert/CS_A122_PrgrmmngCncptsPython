# Week 6, Ch 6, Part 1, Problem 2
# Modifies the largest.py program in the text's Section 6.3.
# Mark both the smallest and largest elements of a list.
# By: Brendan Albert

# createList() function header
def createList():
    # declare values list
    values = []
    # Prime while loop with input, continues until q is entered
    userInput = input('Please enter integer values, Q to quit. ')
    while userInput.upper() != 'Q':
        # build values list by appending int versions of input
        values.append(int(userInput))
        userInput = input('Next int value or Q to quit: ')
    # returns list to location that called it
    return values

# largest() function header
def largest(userList):
    # returns largest element of passed-in arg list
    return max(userList)

# smallest() function header
def smallest(userList):
    # returns smallest element of passed-in arg list
    return min(userList)

# markestList() function's header
def markedList(userList):
    # hold smallest/largest elements of passed-in list
    smallestElement = smallest(userList)
    largestElement = largest(userList)
    print()
    for element in userList:
        print(element, end='')
        if element == smallestElement:
            print(" <== smallest value", end='')
        if element == largestElement:
            print(" <== largest value", end='')
        print()
    print()

# main function header.
def main():
    # call creatList(), return list as argument to markedList
    markedList(createList())

# Entry point
main()
    

    
