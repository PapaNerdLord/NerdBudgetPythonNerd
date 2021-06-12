def payday_function():
    #get payday info from user
    paydayA = input("Hello, Please Enter Payday Amount: ")
    print("Payday Ammount is: " + paydayA)
    
    #convert paydayA to int so you can use it with other ints later
    paydayA = float(paydayA)
    
    #depending on what you make the more you can save.
    if  paydayA >= 300 and paydayA <= 400:
        save_amount = (1/18) * paydayA
        print("Save this much: " + str(save_amount))
    elif paydayA >= 401 and paydayA <= 500:
        save_amount = (1/16) * paydayA
        print("Save this much: " + str(save_amount))
    elif paydayA >= 501 and paydayA <= 600:
        save_amount = (1/14) * paydayA
        print("Save this much: " + str(save_amount))    
    elif paydayA >= 601 and paydayA <= 700:
        save_amount = (1/13) * paydayA
        print("Save this much: " + str(save_amount))
    elif paydayA >= 701 and paydayA <= 800:
        save_amount = (1/12) * paydayA
        print("Save this much: " + str(save_amount))  
    elif paydayA >= 801 and paydayA <= 900:
        save_amount = (1/10) * paydayA
        print("Save this much: " + str(save_amount)) 
    elif paydayA >= 901 and paydayA <= 1000:
        save_amount = (1/8) * paydayA
        print("Save this much: " + str(save_amount)) 
    elif paydayA >= 1001 and paydayA <= 1100:
        save_amount = (1/7) * paydayA
        print("Save this much: " + str(save_amount))             
    elif paydayA >= 1101:
        save_amount = (1/7) * paydayA
        print("Save this much: " + str(save_amount))    

    
payday_function()

#trying to make a menu bar to go in between the functionalities and what not.
def  mainmenu_fuction():
    menu = ["Payday","Options","Exit"]
    mainmenu = input('Main menu? y/n: ')
        mainmenu = str(mainmenu)
        if mainmenu = str("y","Y"):
            print("Main Menu")
            print(me)

mainmenu_fuction()