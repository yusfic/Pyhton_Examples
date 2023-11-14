#This program demontrates calculated payment
#Create main Function 
def main():
    sales = get_sales()
    advanced_pay = get_advanced_pay()
    comm_rate = determine_comm_rate(sales)
    pay = sales * comm_rate -advanced_pay
    print(f'The pay is $ {pay: .2f} ')
    
    if pay<0:
        print('It is wrong calculation')
def get_sales():
    monthly_sales = float(input('Enter monthly sales price: '))
    return monthly_sales

def get_advanced_pay():
    print('Enter the amount of Advance pay, or')
    print('Enter 0 if no advanced pay was given')
    advanced = float(input('Enter advanced pay: '))
    return advanced
    


def determine_comm_rate(sales):
    #Determine the commission rate
    if sales < 10000.0:
        comm_rate = .10
        
    elif sales > 10000.0 and sales <14999.9:
        comm_rate = .12
    elif sales > 15000.0 and sales <17999.9:
        comm_rate = .14
    elif sales > 18000.0 and sales <21999.0:
        comm_rate = .16
        
    else:
        comm_rate = .18
    return comm_rate
   #Call the main function

main()