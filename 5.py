import pandas as pd
data={"names":['ravi','kavi','shani'],
      "Roll no":[101,102,103,],
      "marks":[78,89,90]}
df=pd.DataFrame(data,index=[1,2,3])
print(df)
print(df.loc[2])#loc is used for locating row in dataframe
print(df['names'])
print(df.loc[[1,3]])
