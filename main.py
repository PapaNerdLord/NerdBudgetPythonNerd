def payday_function():
    #get payday info from user
    paydayA = input("Hello, Please Enter Payday Amount: ")
    print("Payday Ammount is: " + paydayA)
    
    #convert paydayA to int so you can use it with other ints later
    paydayA = int(paydayA)
    
    #depending on what you make the more you can save.
    if  paydayA >= 300 and paydayA <= 400:
        save_amount = (1/18) * paydayA
        print("Save this much: " + str(save_amount))
    elif paydayA >= 401 and paydayA <= 500:
        save_amount = (1/16) * paydayA
        print("Save this much: " + str(save_amount))    

payday_function()

def newbills_fuctions():

#Print User Input to A File
#Inputs of Name,Cost,Due day to be write down and pulled back up from file and to be read in another fuction ytbn
#In console to save the cbill amount in total with other bills that I got going.
#My pay day is the 5th and 20th of every month, so if my bills fall after one of those days
#Take all cbills that are due by checking dbill, but not after the other day. Just in their paid periods
nbill = input("Name: ")
cbill = input("Cost: ")
dbill = input("Day of Month: ")
y = open('C:\Users\USERNAME\Documents\Bills.txt', 'w')
y.write(nbill)

#Convert text to binary and then write to file
nbill = input("Enter blah : ")
y = open('C:\Users\USERNAME\Documents\Bills.txt', 'wb')
y.write(nbill)