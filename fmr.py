#WAP:which contains list of numbers.Filter should filter out all such no ..
#..which are greater than or equal to 70 and less than or..
# ..equal to 90(num>=70 & num<=90) .Map function will increase each number by 10..
# ..Reduce will return product of all that numbers.
import functools
def main():
	arr=[]
	size=int(input("Enter size of list :"))
	for i in range(size):
		print("Enter element at index",i+1)
		arr.append(int(input()))
	print("Input_List :",arr)
	Filtered=list(filter(lambda num:(num>=70 and num<=90)==1,arr))
	print("List after filter :",Filtered)	
	Mapped=list(map(lambda num:num+10,Filtered))
	print("List after map :",Mapped)	
	print("Final Output :",int(functools.reduce(lambda no1,no2:no1*no2,Mapped)))
if __name__=="__main__":
	main()
