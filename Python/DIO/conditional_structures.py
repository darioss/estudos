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

string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vitae neque in urna mollis fringilla!!"

print(string[:9]) #print all char between 0 - 9 (9 is out)
print(string[10:]) #print all char between 10 and finish string (finish is out)
print(string[2:14]) #print all char between 2 and 14 positions (14 is out)
print(string[::3]) #print all char of string under step 3 char 9 (finish is out)
print(string[:]) #print complete string
print(string[10:10:2]) #Nothins is printed. 
print(string[::-1]) #print the reversed string.

#triple string or multiline string
name = "Dario Silva"

print(f"TESTE {name[:1]}")

message = f"""
  Hello my name is {name},
I am learning Python.
    This is a incredible programming language."""

print(message)