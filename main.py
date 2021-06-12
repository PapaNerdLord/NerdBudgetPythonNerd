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

