import atexit
start=['Article','First','My']
def cppsecret(start):
	print (start)

for start in start:
# Using function register()
	atexit.register(cppsecret,start)