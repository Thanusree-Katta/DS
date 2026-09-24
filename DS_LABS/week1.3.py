import pandas as pd
"""data={ 'apples':[3,2,0,1], 'oranges':[0,3,7,2]}
df=pd.DataFrame(data,index=['1','2','3','4'])
print(df.loc['2'])"""


"""df =pd.read_csv('iris.csv')
#print(df)
#print(df.head)
#print(df.tail(3))
#print(df.info())
print(df.shape)"""


"""df = pd.read_json('sample1.json', typ='series')
print(df)"""

"""df=pd.read_csv("Iris.csv")
print(df.shape)
dup_df=pd.concat([df, df])
print(dup_df.shape)
dup_df.drop_duplicates(inplace=True)
print(dup_df.shape)
print(df.describe)"""

"""data=[1,2,3,4,5,10,20]
df=pd.DataFrame(data)
#print(df)
df.to_csv('abc.csv',index=True)
print(df)"""

data={'Student_roll':[20,21,22,23,24,25,26,27,28,29], 'name':['abc','bef','cdc','dyx','efc','fhd', 'gij', 'hkl', 'mno', 'pqr'], 'age':[20,21,22,23,24,25,26,27,28,29],'section':['A','B','C','D','E','F','G','H','I','J'],'DS(marks)':[85,90,78,92,88,95,80,87,91,89],'TOC(marks)':[75,80,70,85,78,90,72,88,82,79],'CD(marks)':[80,85,75,90,82,88,78,84,86,81]}
print(pd.DataFrame(data).from_dict(data))
df=pd.DataFrame(data)
df.to_csv('studentdata.csv',index=True)
print(df)
dfstud=pd.read_csv('studentdata.csv')
#print(dfstud.head(3))
#print(dfstud.tail(2))
print(dfstud.info())


