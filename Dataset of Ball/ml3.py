from sklearn import tree 
#Rough 1 #smooth 0 //// #Tennis 1 #cricket 2

def MarvellousML(weight,surface):  

    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
        
    Labele = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
    
    dobj = tree.DecisionTreeClassifier()
    
    dobj.fit(Features, Labele)
    
    result = dobj.predict([[weight, surface]])
    
    if result ==1:
        print("Your object looks like  Tennis ball")
    else:    
        print("Your object looks like Cricket ball")
 
def main():
    print("-----Supervised Machine Learning-----")
    print("Enter the weight of object ")
    weight = int(input())
    print("Enter the Surface of object")
    surface = input()
    
    if surface.lower() == "rough":
        surface = 1
    elif surface.lower() == "smooth":
        surface =0
    else:
        print("Invalid input")
        return 
        
    MarvellousML(weight , surface)
 
if __name__ == "__main__":
    main()