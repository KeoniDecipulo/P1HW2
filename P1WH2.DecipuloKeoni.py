#Keoni Decipulo
#4/7/24
#P1WH2
#Using Python's input and print functions with 7 variables
#adding math sequences to calculate a person's left over money
#from a trip
print('This Program calculates and displays travel expenses')
print('')
budget=int(input('Enter your budget:'))
print('')
travel_destination=input('Enter your travel destination:')
print('')
gas_amount=int(input('Amount you will spend on gas:'))
print('')
accommodation=int(input('Amount you will spend on accommodation:'))
food_amount=int(input('Amount you will spend on food:'))
print('')
expenses=int(gas_amount+accommodation+food_amount)
End_result=int(budget-expenses)
print('------------Travel Expenses------------')
print('Location:', travel_destination)
print('Initial Budget:', budget)
print('')
print('Fuel:',gas_amount)
print('Accomodation;',accommodation)
print('Food:',food_amount)
print('')

#print('Expenses total:', expenses)
print('Remaining Balance', End_result)
