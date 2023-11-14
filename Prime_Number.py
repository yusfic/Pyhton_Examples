#PRIME NUMBER(Q1)
#This program demonstrates Prime Number
#Prime number which is divisible by 1 and itself is called prime number
#Otherwise it is not prime number

#Create main function
def main():
    
    num = int(input('Enter a number: ')) # Enter integer Number
    
    result = prime(num)                  # Call prime function and assign variable
    
    print(f'Here is your number {num}. Is it Prime Number? {result}')  # Display result !!!
    
#Create prime function for control 
def prime(num):
    #If any Number is divisible by n between 2 to n-1 we can say it is not prime number otherwise it is prime number!
    for i in range(2,num): #Initialize a for loop starting from 2 ending 
                           #One less than the entered Value

        if num % i == 0:   #Check if entered number divisible except from itself and 1
            return False   #If it can divide another number return False !
        
    else:
        return True        #Otherwise return True !
    
#Call main Function !
main()