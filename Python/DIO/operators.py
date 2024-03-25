#Arithmethic operators
product1 = 100
product2 = 20

print(product1 - product2) # print 80
print(product1 + product2) # print 120
print(product1 * product2) # print 2000
print(product1 ** product2) # print 1x10^40
print(product1 / product2) # print 5.0
print(product1 // product2) # print 5
print(product1 % product2) # print 0

print(product1 * 10 + (5* (product2-7))) #print 1065

#Compare operators
print(product1 == product2) # print False
print(product1 < product2) #print False
print(product1 > product2) #print True
print(product1 <= product2) #print False
print(product1 >= product2) #print True

# Assingn operators
product3 = 10
print(product3) #print 10

product3 += 40
print(product3) #print 50

product3 -=20
print(product3) #print 30

product3 //= 5
print(product3) #print 6

product3 /= 3
print(product3) #print 2.0

product3 *= 10
print(product3) #print 20.0

product3 %= 3
print(product3) #print 2

product3 **= 5
print(product3) #print 32

#Logic operators
# And - return True only all conditions returning True
print(True and True) #print True
print(True and False) #print False
print(False and False) #print False

#OR - return False only all conditions returning False
print(True or False) #print True
print(True or True) #print True
print(False or False) #print False

#Two condition need return true for result true
print(product1 > product3 and product2 > product3) #Return False

#Only one condition need return true
print(product3 > product2 or product1 >= product2) #Return True

#Reject operation
print(not product3 > product1) #Return True
print(not product3 < product1) #Return False

print((product1 > product3 and product2 > product3) or (product3 > product2 or product1 >= product2)) #Print True

#Identity operators
#Verify if two elements occupy the same memory region
product4 = product3
print("-----")
print(product4 is product3) #Return True
print(product4 is not product3) #Return False
print(product4 is product1) #Return False

#Associate operators (Case sensitive)
#Verify if a object is present on sequence
products = ["Pen", "Pencil", "Ruller"]
print(products)
print("Pen" in products) #return True
print("Erase" not in products) #return True
print("Pencil" not in products) #return False
print("Erase" in products) #return False
print("ruller" in products) #return False

name = "Joseph Smith Wood"
print("Joseph" in name) #return True
print("Woodstock" not in name) #return True
