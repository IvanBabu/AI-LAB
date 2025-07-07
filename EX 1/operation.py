a=int(input("Enter 1st variable "))
b=int(input("Enter 2nd variable "))
print("sum", a+b)
print("Difference", a-b)
print("product", a*b)
try :
	print("Quotient is ", a/b)
except ZeroDivisionError:
	print("Division by zero not possible")
if b!=0:
	print("Floor division quotient:", a/b)
else:
	print("Division by zero not possible")
try:
	print("remaider is ", a%b)
except ZeroDivisionError:
	print("Modulo", a%b)
print("Expone is ", a**b)
