from sklearn import tree 
#Rough 1 #smooth 0 //// #Tennis 1 #cricket 2

def main():

    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
        
    Labele = [14,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
    
    dobj = tree.DecisionTreeClassifier()
    
    dobj.fit(Features, Labele)
    
    result = dobj.predict([[40,1]])
    
    print("Ball is ",result)
    
if __name__ == "__main__":
    main()