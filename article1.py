import atexit
names=['Article','First','My']
def cppsecret(name):
	print (name)

for name in names:
# Using function register()
	atexit.register(cppsecret,name)