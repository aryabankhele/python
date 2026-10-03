a = int(input("enter a : "))
b = int(input("enter b : "))
temp = a  #add a third variable temp to store the old value of a
a = b
b = temp
print("a :" , a)
print("b :" , b)