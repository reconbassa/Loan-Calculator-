print('Welcome to the loan estimator tool or "LET" for short. You can use this tool to calculate your estimated monthly paymemts for your desired loan amount. ')

loan = input('What is the loan amount you would like to take out? ')
loan = float(loan)
interest = input('How much would you like to pay in interest?/n I.E., 10% = 10, 15% = 15, 25% = 25.  ')
interest = float(interest)/100
years = input('How many years would you like length of the loan to be? /n I.E., 1,2,3 etc ')
years = float(years) *12
PayLength = (loan / years)
print('Perfect! Below is the loan option we have come up with for you')
MonthlyPayment = PayLength + interest*PayLength
float(MonthlyPayment)

print(MonthlyPayment)


