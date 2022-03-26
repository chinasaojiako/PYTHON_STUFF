#Take the luggage details of the customer
#print('How many luggage do you have please?')
#luggage_count = int(input())
print('What is the weight in kg of your luggage?')
luggage_weight = int(input())

#Conditions to be met
Luggage_max = 50
cost_per_kg_for_below_equal_50 = 2
cost_per_kg_for_above_50 = 5

luggage_diff = luggage_weight - Luggage_max

if luggage_diff > 0 :
	cost = (luggage_diff * 5 + (Luggage_max * 2))
	print('The cost of your luggage is ' + str(cost) + ' because your luggage has an excess of ' + str(luggage_diff) + ' kg. Our company charges 5 per kg for excess weight over 50 kg.')
elif luggage_diff <= 0 :
	cost = luggage_weight * 2
	print('The cost of your luggage is ' + str(cost) + ' because your luggage was less than the maximum weight limit by ' + str(luggage_diff * -1) + ' kg. Our company charges 2 per kg for luggage weight less than 50 kg.')
