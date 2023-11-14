#This program simulates the rolling of dice
import random
#Constants for min and max numbers
min = 1
max = 6
def main():
    #Create a variable for control the loop
    again = 'y'
    #Simulate rolling of dice
    while again == 'y' or again == 'Y':
        print('Rolling the dice...')
        print('Their values are: ')
        print(random.randint(min,max)) #dice throw 1
        print(random.randint(min,max)) #dice throw 2
        #Ask the user for another roll of the dice
        again = input('Do you wanna play again(y or n): ')
#Call the main function        
main()
