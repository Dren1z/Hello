'''
this program allows for choosing between two financial calculators
- investment calculator
- home loan repayment calculator

The user should choose one of the two.

variables:
cal         - which calculator is selected
interest    - simple or compound interest type

investment calculator:
    P       - the amount of money the client depositing
    r       - yearly interest rate in %
    t       - number of years plan on investing
    A       - the total amount once the interest has been applied

home loan repayment calculator:
    P       - present value of the house
    i       - monthly interest rate in %
    n       - number of months over which the bond will be paid
    re      - the repayment needed each month
'''

import math

print("investment   - to calculate the amount of interest you'll earn on your investment")
print("bond         - to calculate the amount you'll have to pay on a home loan")

cal = input("Enter either 'investment' or 'bond' from the menu above to proceed: ") # choice of a calculator

#investment calculator
if cal.lower() == "investment":  # covert into lower case to be case insensitive
    P = float(input("The amount of money you are depositing: "))
    r = float(input("The interest rate in %: "))
    t  = int(input("The number of years you plan on investing: "))
    interest = (input("Is it a simple or compound interest? "))

    # calculate total amount
    if interest.lower() == "simple": # covert into lower case to be case insensitive
        A = P * (1 + r/100*t)
        print("The total amount is {}.".format(A))
    elif interest.lower() == "compound":
        A = P * math.pow(1 + r/100, t)
        print("The total amount is {}.".format(A))


# home loan repayment calculator
elif cal.lower() == "bond": # covert into lower case to be case insensitive
    P = float(input("The present value of the house: "))
    i = float(input("Monthly interest rate in %: "))
    n = int(input("Number of months over which the bond will be repaid: "))

    re = round((i/100*P)/1-math.pow(1 + i/100,-n),2) # calculate repayment
    print(f"The amount you will have to repay each month is {re}.")

else: # if neither calculator was selected
    print("You did not enter a valid calculator. Exiting the program.")