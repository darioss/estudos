#Format text Case
text = "PyThOn"
print(text.upper()) #To uppercase
print(text.lower()) #To LowerCase
print(text.title()) #To Capitalize

#Remove with spaces
other_text = "      Python "
print(other_text.strip()) #Remove All
print(other_text.lstrip()) #Remove Left
print(other_text.rstrip()) #Remove Right

#Join and Center
print(text.center(80,"*")) #Centered text on 80 characters space, adding "*"
                           # if character not defined, text is centered of white line
print(".".join(text)) #Add "." between  letters of text

PI = 3.1415
print(f"The PI Value is {PI:.2f}, represented with two points decimals.")
name = "Dario Silva"
age = 44
profession = "programmer"

print(f"Hi, I am {name}. My age is {age} years and my profession is {profession}. Thanks for contact me.")

