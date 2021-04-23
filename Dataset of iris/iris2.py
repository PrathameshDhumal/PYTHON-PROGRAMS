from sklearn.datasets import load_iris

def main():
    dataset = load_iris()
    
    print("Features of datasets")
    print(dataset.feature_names)

    print("Target names of datasets")
    print(dataset.target_names)
    
    print("Iris data set is:")
    
    for iCnt in range(len(dataset.target)):
        print("ID: %d Feature:%s Label: %s "%(iCnt,dataset.data[iCnt],dataset.target[iCnt]))
if __name__ == "__main__":
    main()