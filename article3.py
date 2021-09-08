import atexit
def cpp():
	print("registered")
def cpp1():

	print("unregister")
atexit.register(cpp)
atexit.register(cpp1)
atexit.unregister(cpp)