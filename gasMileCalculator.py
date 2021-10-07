#!/user/bin/env python 3

#User inputs
#inputs will be used for equations
milesDriven = int(input("Input miles driven "))
                
gallons = int(input("Input gallons used "))

costPerGallon = float(input("Cost Per Gallon "))


#equation for miles driven 
mpg = milesDriven / gallons

#equation for total fuel cost
totalFuelCost = gallons * costPerGallon

#equation for cost per mile
costPerMile = totalFuelCost / milesDriven



#Display Outputs
                      
print("Your miles per gallon is " , ( mpg))

print("The total cost of your trip is $" , (totalFuelCost))

print("The cost per mile is", (costPerMile))

