# Define the function that parse through the filename and checks if customers overpayed or underpayed
def new_customer(filename):

    # Set cost of melon
    melon_cost = 1.00

    # Open the file with customer information
    import_file = open(filename)

    # Loop through each line of the file, tokenize it and check which customers overpayed or underpayed
    for line in import_file:

        # Tokenize each line into an array
        token = line.rsplit('|')

        # Extract name, number of melons purchased and amount paid for each customer
        customer_name = token[1]
        customer_melons = int(token[2])
        customer_paid = float(token[3])

        # Calculate how much the customer should have paid
        customer_expected = customer_melons * melon_cost

        # Check how much each customer paid and print whether they overpayed or underpayed
        if customer_paid < customer_expected:
            print(f"{customer_name} underpayed")
        elif customer_paid > customer_expected:
            print(f"{customer_name} overpayed")
        else:
            print(f"{customer_name} paid the right amount")

    # Close the file
    import_file.close()


# Finally call the function to run it!
new_customer('customer-orders.txt')
