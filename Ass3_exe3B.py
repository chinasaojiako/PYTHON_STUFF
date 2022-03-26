#WHAT IS THERE ARE MANY LUGGAGE OF VARIOUS WEIGHT?

#Take the luggage details of the customer
print('How many luggage do you have please?')
luggage_count = int(input())
print('What is the weight in kg of your luggage?')
luggage_weight1 = int(input())
luggage_weight2 = int(input())
luggage_weight3 = int(input())

#Conditions to be met
Luggage_max = 50
cost_per_kg_for_below_equal_50 = 2
cost_per_kg_for_above_50 = 5

luggage_diff = luggage_weight - Luggage_max

if luggage_diff > 0 :
	cost = luggage_diff * 5