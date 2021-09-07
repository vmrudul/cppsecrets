import atexit
sum=0
@atexit.register
def addition(sum,a):
	add=sum+a
	return add
def sub(sum,s):
	sub=sum-s
	return sub
def view():
	return sum

while True:
	n=int(input("Enter 1 for addition ,Enter 2 for substraction,Enter 3 to view total calculation, Enter 4 to exit "))
	if n==1:
		a=int(input("Enter number to be added "))
		sum=addition(sum,a)
		print("addition is ",sum)
		
	elif n==2:
		s=int(input("Enter number to be substracted "))
		sum=sub(sum,s)
		print("substraction is ",sum)
	elif n==3:
		print(sum)
	else:
		break 