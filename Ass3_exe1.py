#We need to enter two numbers
print('Enter two numeric values')
a = int(input())
b = int(input())

#Finding out or verifying if the second number is even or odd
even = b%2 == 0
odd = b%2 != 0
print(even)
print(odd)

#Another way of verifying whether even or odd is to use an if-else condition statement as shown below
#if (b % 2 == 0):
    #print ('b is even')
#else:
	#print('b is odd')

#We write the first conditional statement
if (a < 5) or (even == True):
    print('At least one condition has been satisfied')

#We write the second conditional statement
if (a >= 5) and (odd == True):
	print('No condition has been satisfied')

#Combining the two conditional statements using and if-elif statement
if (a < 5) or (even == True):
    print('At least one condition has been satisfied')
elif (a >= 5) and (odd == True):
	print('No condition has been satisfied')