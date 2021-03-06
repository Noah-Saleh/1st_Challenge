# coding: utf-8

import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""

loan_costs = [                #cost of 5 different loans in ($)
               500 ,
               600 ,
               200 ,
              1000 ,
               450 , 
             ]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
# YOUR CODE HERE!

number_of_loans = len(loan_costs)       # the len function counts the number of indicies in the list to give us
                                        # the number of loans     

print(          )        
print( "--------------------------------------------------------------------" ) # a line to help separate things
print(          )
print( "PART 1" )                                           # a title for this section
print(          )
print(          )                                           # printing some blank lines to make things easy to read
print(f"Total number of loans:        {number_of_loans}" )

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# YOUR CODE HERE!

total_value_of_loans = sum(loan_costs)     # The sum function sums together the value of each index together.
                                           # So, we are adding the values of all the          loans together. 
print(                                                        )
print(f"Total value  of loans:    ${total_value_of_loans}.00" )

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
# YOUR CODE HERE!

average_loan_amount = total_value_of_loans / number_of_loans    # calculating the average loan amount

print(                                                      )
print(f"Average loan amount  :    $ {average_loan_amount}0" )
print(                                                      )
print("---------------------------------------------------------------------")

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan

loan  =  {                                                      # detailed data for a loan
           "loan_price"         :      500  ,      # in ($)
           "remaining_months"   :        9  ,
           "repayment_interval" :  "bullet" ,
           "future_value"       :     1000  ,      # in ($)
         }

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!

future_value       = loan.get (             # using the get function to retrieve the value assosiated with the
"future_value"                )             # key "future value"

remaining_months   = loan.get (             # using the get function to retrieve the value assosiated with the
"remaining_months"            )             # key "future value"

print(          )
print( "PART 2" )
print(          )
print(                                        )
print(f"Future value    :    ${future_value}" )                     # printing the retrieved future    value
print(                                                      )
print(f"Remaining months:        {remaining_months} months" )       # printing the retrieved remaining months

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
# YOUR CODE HERE!

present_value = round (                                                  # creating a formula for the present_value
                        future_value / (1 + 0.2/12)**remaining_months    # variable using the present value formula
                  , 2 )

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value (SHOULDN'T THIS READ "THE CURRENT COST" INSTEAD OF 
# THE PRESENT VALUE? I THOUGHT PRESENT VALUE IS THE SAME THING AS "FAIR VALUE".) represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

loan_price   = loan.get (       # using the get function to retrieve the value assosiated with the key "loan_price"
"loan_price"            )

print        (                                                                             )
if present_value >= loan_price :                       # conditional logic analyzing whether or not to buy the loan
       print (                                                                             )
       print (f"Fair value of loan:                            ${present_value}"           )
       print (                                                                             )
       print (f"The loan is worth at least the cost to buy it (${loan_price}.00)."         )
       print ("So, it would make sense to buy this loan."                                  )
else :
       print (                                                                             )
       print (f"Fair value of loan:                                     ${present_value}"  )
       print (                                                                             )
       print ( "The loan is too expensive and not worth the price"                         )
       print (f", since the fair value is less than the cost to buy it (${loan_price}.00)" )
print        (                                                                             )
print        ( "----------------------------------------------------------------------------------" )

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan

new_loan =   {                                     # new loan's data organized in a dictionary
               "loan_price"         :     800  ,
               "remaining_months"   :      12  ,
               "repayment_interval" : "bullet" ,
               "future_value"       :    1000  ,
             }

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!

print(          )
print( "PART 3" )
print(          )
print(          )

def  present_value   (                              # defining a function to calculate the present value of
                       future_value         ,       # a loan based of 3 parameters/variables
                       remaining_months     ,
                       annual_discount_rate ,       #this makes it easier to calculate the present values of many loans
                     ):

     present_value = future_value / (1 + annual_discount_rate/12)**remaining_months

     return present_value                           # this tells the function, when called, 
                                                    # to return the resulting calculation inside the code
                                                    # (not to print the result)

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!

present_value =                                   round   (              #Calling the present_value function. Note: you
present_value                                           (                #don't have to put "parameter=" when entering in
                  future_value         = new_loan.get (                  #the arguments of a function
                 "future_value"                       ) ,

                  remaining_months     = new_loan.get (
                 "remaining_months"                   ) ,  

                  annual_discount_rate =              (
                 0.2                                  ) 
                                                        ) ,
                 2                                        )              #we round the result to 2 decimal places
                
print (f"The present value of the loan is: ${present_value}" )
print (                                                      )
print ( "--------------------------------------------------------------" )

"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans =  [                                       #a list of dictionaries containingd detailed loan info
           {
             "loan_price"         :      700  ,
             "remaining_months"   :        9  ,
             "repayment_interval" : "monthly" ,
             "future_value"       :     1000  ,
           }                                  ,
           {
             "loan_price"         :      500  ,
             "remaining_months"   :       13  ,
             "repayment_interval" :  "bullet" ,
             "future_value"       :     1000  ,
           }                                  ,
           {
             "loan_price"         :      200  ,
             "remaining_months"   :       16  ,
             "repayment_interval" :  "bullet" ,
             "future_value"       :     1000  ,
           }                                  ,
           {
             "loan_price"         :      900  ,
             "remaining_months"   :       16  ,
             "repayment_interval" :  "bullet" ,
             "future_value"       :     1000  ,
           }                                  ,
         ]

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!

inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!

for loan in (                                #for loop to repeat the process for every dictoinary in the "loans" list
    loans   )  :                       
                 if loan.get    (               #conditional logic to filter out the expensive loans
                   "loan_price" ) <= 500   :
                                             inexpensive_loans.append (       #adding all the inexpensive loans to a list
                                             loan                     )

# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!

print                         (          )
print                         ( "PART 4" )
print                         (          )
print                         (          )

for         loan  in (                           #For loop to print every inexpensive loan. This keeps the data more
inexpensive_loans    ) :                         #organized than if you were to simply do print(inexpensive_loans)
                         print(   loan   )
                         print(          )

print                         ( "-----------------------------------------------------------------------------------------------------------" )
print                         (          )

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header

header = [ "loan_price" , "remaining_months" , "repayment_interval" , "future_value" ] #a header for the csv file

# Set the output file path

output_path = Path("inexpensive_loans.csv")               #using the Path tool from pathlib to get the file path for the csv

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!

with open(output_path , 'w' , newline='') as csvfile :    #this specifies where and what file we are writing to

     csvwriter = csv.writer(csvfile)                      #creating a short variable name so we don't
                                                          #have to retype csv.writer(csvfile)
     csvwriter.writerow(header)                           #EvERy sInGLe time we want to use it (DRY)

     for loan in inexpensive_loans :                      #for loop to write every single dictionary as a row in the csvfile
         csvwriter.writerow(loan.values())