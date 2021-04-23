#WAP: Accept parameter and return the value
def fun():
    print("inside fun")
    
def gun(value):
    print("Inside Gun",value)

def sun(value):
	value = value+1
	print("Inside sun")
	return value
	
def mun():
	pass
	
def outer():
	print("Inside outer")
	def inner():
		print("inside inner")
	inner()

def main():
	fun()
	gun(11)
	ret=sun(10)
	print(ret)
	mun()
    inner()
	outer()
    
if __name__ == "__main__":
    main()