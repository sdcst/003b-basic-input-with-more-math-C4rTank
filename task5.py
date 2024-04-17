#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1
#Enter the number of days: 12
#There will be 25017087 people after 12 days

import math

cp = input("Enter the current population :")
r = input("Enter the rate of growth as a decimal :")
d = input("Enter the number of days :")

cp = float(cp)
r = float(r)
d = float(d)

percent = r/100
step1 = 1 + percent
step2 = step1**d
step3 = cp * step2
fp = str(step3)

print("There is going to be",fp,"people after",d,"days!")