
def savings_percentage_options_function()

# dpaid = days paid, like you get paid twice a month or three times a month.
	
	print("Current amount of paydays with in a month is " + dpaid + " times a month.")


savings_percentage_options_function()







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
#I want to write more then one thing but being able to recall them back as independent variables
y.write(nbill)

#Convert text to binary and then write to file
#Guess this has to exist i dont know i was skimming and reading bits and piecees
nbill = input("Name: ")
cbill = input("Cost: ")
dbill = input("Day of Month: ")
y = open('C:\Users\USERNAME\Documents\Bills.txt', 'wb')
#I want to write more then one thing but being able to recall them back as independent variables
y.write(nbill)

newbills_fuctions()