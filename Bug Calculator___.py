#Bug collector
total = 0
days = int(input('Enter your days: '))
for i in range(1,days + 1): # 1 2 3 4 5 
    print(f' here is the day{i}')
    print('-----------------')
    num_of_col_bugs = int(input('how many bugs did you collect: '))
    print('-------------------')
    total = total + num_of_col_bugs
    
print(f'Here is your total bug {total} and it collected for {days}')

#