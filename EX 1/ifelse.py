n=int(input("Enter the marks(out of 100):"))
if n>=90:
	print("Grade A")
elif n<90 and n>=75:
	print("Grade B")
elif n<75 and n>=60:
	print("Grade c")
elif n<60 and n>=40:
	print("Grade D")
else:
	print("Faild")
