#Leap Year
#Enter year 
year = int(input('Enter the year:'))
#Calculate leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'In {year} February has 29 days')
    
else:
    print(f'In {year} February has 28 days')
