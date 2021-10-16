import os
while True:
	op=int(input("1. create, 2.remove, 3.write, 4.read, and 5.exit "))
	if op==1:
		filename=input("senter filename to create ")
		if os.path.exists(filename):
			print(filename,"already exists ")
		else:
			f=None
			try:
				f=open(filename,"a")
				print(filename,"created")
			except Exception as e:
				print("creation issue ",e)
			finally:
				if f is not None:
					f.close()
	elif op==2:
		filename=input("enter filename to remove ")
		if os.path.exists(filename):
			os.remove(filename)
			print(filename,"removed")
		else:
			print(filename,"does not exists")
	elif op==3:
		filename=input("enter filename to write ")
		if os.path.isfile(filename):
			f=None
			try:
				f=open(filename,"w")
				data=input("enter data to write ")
				f.write(data + "\n")
			except Exception as e:
				print("writing issue ",e)
			finally:
				if f is not None:
					f.close()
		else:
			print(filename,"does not exista")
	elif op==4:
		filename=input("enter filename to read from ")
		if os.path.isfile(filename):
			f=None
			try:
				with open(filename,"r") as f:
					data=f.read()
					print(data)
			except Exception as e:
				print("reading issue ", e)
		else:
			print(filename ,"does not exist")
	elif op==5:
		break
	else:
		print("invalid input") 
