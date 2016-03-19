# Week 7, Chapters 1-6, Extra Credit, Part 2, Problem 3
# Build two lists, tracking customers' names and sales
# The sales are calculated and the name of the best customer
# of the day is printed.
# By: Brendan Albert

# Define nameOfBestCustomer function header.
# Function accepts two lists as arguments.
# Checks for and returns name of best customer.
def nameOfBestCustomer(sales, customers):

    # Declare/Initialize variable to keep track of highest sale
    maxSale = sales[0]
    # variable to return when the best customer is found
    bestCustomer = customers[0]
    # for loop which goes through all the sales and associates the highest sale with the respective customer
    for idx in range(1, len(sales)):
        # if this particular sale is the highest seen so far, make that the new highest sale...
        if sales[idx] > maxSale:
            maxSale = sales[idx]
            # ... and assign new bestCustomer name.
            bestCustomer = customers[idx]
    # return the name of the best customer
    return bestCustomer
            
# Declare main function header
def main():

    # Declare / initialize sales and customers lists
    salesList = []
    customersList = []
    # Prime while loop with a sales amount other than 0.
    sales = -1
    # While-loop which prompts user for sales and names while the sales amount is not the sentinel 0
    while sales != 0:
        # Get sales input
        sales = float(input("Enter Sales (0 to quit): "))
        # if sentinel 0 is entered, this if-block is bypassed
        if sales != 0:
            # Otherwise, append the sales amount to the salesList
            salesList.append(sales)
            # Prompt for customer name to associate with the sale
            customer = input("Enter customer: ")
            # Add customer name to customersList
            customersList.append(customer)
    # Once the sentinel 0 is entered, we call this print function which calls the nameOfBestCustomer function.
    # The nameOfBestCustomer function is passed the two lists and will return the name of today's best customer.
    print("Today's best customer is", nameOfBestCustomer(salesList, customersList), "!")

# Call main function, program entry-point
main()
