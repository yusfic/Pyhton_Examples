#This program displays property taxes
TAX_FACTOR = 0.0065

#Get the first lot number
print('Enter the property lot number')
print('or Enter 0 to end:   ')
lot = int(input('Enter lot number: '))

#Continue processing as long as user
#does not enter the number 0

while lot != 0:
    #Get the property value
    value = float(input('Enter the property value'))
    #Calculate the tax
    tax = value * TAX_FACTOR
    #Displays the Tax
    print(f'Here is your tax {tax: .2f}',sep='')
    #Get the another lot number
    print('Enter the next property lot number')
    print('or Enter 0 to end:   ')
    lot = int(input('Enter lot number: '))
    
print('End')