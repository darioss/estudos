def cash(value):
    balance = 500

    if (balance >= value):
        balance -=value
        print (f"You successfully cashed {value}! Your new balance is {balance}")
    else:
        print ("Your balance is insufficient")  

cash(100)
cash(600)


#Other sample using ternary
#Ternary if
balance = 500
value = 100
status = "Sucess!" if balance > value else "Fail!" 
print(status) 