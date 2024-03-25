# FOR / FOR - ELSE
text = input("Whats is your message?\n")
vowels = "aeiou"
for char in text:
  if char in vowels:
    print(char, end=" - ")
else: #Else is optonal
  print("\nThis is a for - else")

# RANG - The first element is included, but the last, not.
range_number = list(range(100)) # Create list number betwenn 0 - 99
print(f"List of numbers: {range_number}\n\n")

for number in range(20, 85, 2): #print from 20 to 84 (the last argument is a step length) (start, stop, step)
  print(number, end=" - ")
else:
  print("\nFor using Range Method")

#While / While - Else
option = -1
while option != 0:
  option = int(input("[1] Cash \n[2] account statement \n[0] exit \n:"))
  if option == 1:
    print("Cashing...")
  elif option == 2:
    print("Showing account statement...")
  else:
    if option != 0:
      print("Invalid option. Select other, please.")
else:
  print("Thank you for use this system")

# Break reserved word
while True: #infinite loop
  number = int(input("Please, digit a random number: \n"))
  if number == 10: # condition for scape of lopp
    print("Congrats, you luck!")
    break
  
  if number%2 == 0:
    continue
  
  print(number)