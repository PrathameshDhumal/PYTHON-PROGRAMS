import os
def main():
	print("Inside main")
	print("Number of cpu cores are :",os.cpu_count())
	
if __name__ == "__main__":
	main()