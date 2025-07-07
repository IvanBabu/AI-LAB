while True:
	a=int(input("Enter the 1st no"))
	b=int(input("Enter the 2nd no"))
	c=input("Enter the operators(+,-,/,*):")
	if c=='+':
		print("Sum is:", a+b)
	elif c=='-':
		print("Diff is:", a-b)
	elif c=='*':
		print("Product is:", a*b)
	elif c=='/':
		if(b!=0):
			print("Quotient is:", a/b)
		else:
			print("Division by zero ")
	elif c=='0':
		break;
	else:
		print("Invalid")
