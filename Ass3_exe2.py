#First, I need to collect the required data from the loan applicant
print('Enter your name please')
name = input()
print('Enter your year of birth please')
year_of_birth = int(input())
print('Enter requested loan amount please')
loan_amount_request = int(input())
print('Enter your annual salary please')
annual_salary = int(input())
print('Enter current debt if any, please')
current_debt = int(input())

#Write the conditions that must be met for loan to be granted
#Applicant's age
age = 2022 - year_of_birth

#Applicant's loan request limit
amount = 0.5 * annual_salary
print(name + ', your loan request limit is £' + str(amount))

#Applicant's debt limit
debt_limit = (20 / 100) * loan_amount_request
print(name + ', your debt limit is £' + str(debt_limit))

#Write an if-elif-else statement to put everything together
if age <= 18 :
	print(name + ', you are too young to take loan')
elif loan_amount_request > amount :
    print('Sorry ' + name + '. Your loan application for £' + str(loan_amount_request) + ' has been rejected')
elif current_debt < debt_limit :
	print('Congratulation ' + name + '! Your loan application for £' + str(loan_amount_request) + ' has been approved')
else:
	print('Sorry ' + name + '. Your loan application for £' + str(loan_amount_request) + ' has been rejected')

