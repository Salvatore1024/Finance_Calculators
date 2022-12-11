#Finance calculators:

#Import the math function.
import math

#Display to the user the possible choices to pick up.
print("\nChoose either 'investment' or  'bond' from the menu below to proceed: "
      "\ninvestment - to calculate the amount of interest you'll earn on your investment"
      "\nbond       - to calculate the amount you'll have to pay on a home loan")

#Request from the user their choice.
user_choice = input("\nEnter your choice: ").lower()

#Create a flow control structure based on if-elif-else statements plus an if and else statements nested inside the
#structure. This more complex structure is useful to cover all the possibilities that we could face. The cases are:
#1) If the user enters a wrong input, we should give back a message of error.
#2) If the user choices "investment" we should request other inputs and one of these is " interest_type". Depending
#on the interest type we will have 2 different outputs to print out. It is in this case that we use the nested
#if and else statements. The outputs(investment_return_values) printed out will be different depending
#on which type of interest the user chose.
#3)The last case considered is if the user choices "bond". In this case we will print out the monthly and total amount
#that the user will have to repay.

if user_choice == "investment":
    money_amount = float(input("Enter how much money you would like to deposit: "))
    interest_rate = float(input("Enter your interest rate(only the number without '%' symbol): "))
    p_rate = interest_rate / 100
    years_plan = float(input("Enter for how many years you would like to invest: "))
    interest_type = input("Choose either your interests to be 'simple' or  'compound': ").lower()
    if interest_type == "simple":
        investment_return_value = round(money_amount*(1+p_rate*years_plan), 2)
        print(f"Your return value at the end of the investment will be: {investment_return_value}")
    else:
        investment_return_value = round(money_amount*(math.pow((1+p_rate), years_plan)), 2)
        print(f"Your return value at the end of the investment will be: {investment_return_value}")
elif user_choice == "bond":
    house_value = float(input("Enter the present value of your house: "))
    interest_rate = float(input("Enter your interest rate(only the number without '%' symbol: "))
    monthly_int_rate = interest_rate/100/12
    months_num = float(input("Enter the number of months you plan to take to repay the bond: "))
    monthly_repayment = round((monthly_int_rate*house_value)/(1-(1+monthly_int_rate)**(-months_num)), 2)
    total_repayment = round((monthly_repayment*months_num), 2)
    print(f"Your monthly amount to repay the bond will be {monthly_repayment}")
    print(f"The total amount to repay at the end of the bond's duration "
          f"will be {total_repayment}")
else:
    print("Error! You didn't enter a right selection. Try it again.")
