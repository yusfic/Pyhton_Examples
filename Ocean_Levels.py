#This program Calculates Ocean Levels
#Constants
rise_ocean_per_year = 1.6 #milimeters 
#Total variable
total = 0
for i in range(1,26):
    #Calculates ocean levels
    total_rise = i * rise_ocean_per_year 
    print(f'Ocean Level Rising is {total_rise: .1f} for This Year {i}  ')
    total = total + total_rise
print(f'Here is the Ocean Level rising after 25 years {total: .1f}')