class Univariate:
    def QuanQual(dataset):
        Quan = []
        Qual = []
        for columnName in dataset.columns:
            if dataset[columnName].dtypes == 'O':
                Qual.append(columnName)
            else:
                Quan.append(columnName)
        return Quan, Qual

    # identif the outlier column Names
    
    def outliercolumnName:
    lesser=[]
    greater=[]
    for columnName in quan:
        if descriptive[columnName]["Min"]<descriptive[columnName]["Lesser"]:
            lesser.append(columnName)
        if descriptive[columnName]["Max"]>descriptive[columnName]["Greater"]:
            greater.append(columnName)
    retern lesser,greater
    
    #Removed the outliers
    
    def outlierremoved:
    for columnName in lesser:
        dataset[columnName][dataset[columnName]<descriptive[columnName]["Lesser"]]=descriptive[columnName]["Lesser"]
    for columnName in greater:
        dataset[columnName][dataset[columnName]>descriptive[columnName]["Greater"]]=descriptive[columnName]["Greater"]
    return outlierremoved

    # identify the Frequence,Relative frequence & Cumulative Relative frequence

    def freqTable(columnName,dataset):
        freqTable =pd.DataFrame(columns=["Unique_value","frequence","Relative_frequence","cumsum"])
        freqTable["Unique_value"]=dataset[columnName].value_counts().index
        freqTable["frequence"]=dataset[columnName].value_counts().values
        freqTable["Relative_frequence"]=freqTable["frequence"]*103
        freqTable["cumsum"]=freqTable["Relative_frequence"].cumsum()
        return freqTable
    
    # After removed the outliers of Dataset
    def Univariate(dataset,quan):

    descriptive= pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%",
                                 "IQR","1.5 Rule","Lesser","Greater","Min","Max"],columns=quan)
    for columnName in quan:
        descriptive[columnName]["Mean"]=dataset[columnName].mean()
        descriptive[columnName]["Median"]=dataset[columnName].median()
        descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
        descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
        descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
        descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
        descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
        descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
        descriptive[columnName]["1.5 Rule"]=1.5*descriptive[columnName]["IQR"]
        descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5 Rule"]
        descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5 Rule"]
        descriptive[columnName]["Min"]=dataset[columnName].min()
        descriptive[columnName]["Max"]=dataset[columnName].max()
    return descriptive
    
