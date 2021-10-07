#!/user/bin/env python 3

#application that will allow the user to enter
#the number of text messages sent in the last month.
#Messages are 0.25 each and a 9% tax is added to the total.


#Get User Input
text = int(input("Enter TextMessages Sent:"))


#Text Messages are 0.25 each
textMsg = 0.25
    
#Tax is 0.09
SALES_TAX = 0.09

#multiply text and textMsg, then add SALES_TAX
total = (text * textMsg) + SALES_TAX


#Display User Input
print("Your Total is: ", (total))
