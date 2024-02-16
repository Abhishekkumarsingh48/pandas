#creatin a df using dictionary of series
import pandas as pd
import numpy as np
s1=pd.Series(['Abhishek','Ansh','Aman'])
s2=pd.Series([102,103,104])
s3=pd.Series([11,34,67])
ds={"name":s1,"Roll_no":s2,"marks":s3}
df1=pd.DataFrame(ds)
#print(df1)
#print(df1.columns)
df1["Adress"]=["Delhi","Noida","Goa"]
#print(df1)
#insert(location,column_name,column_value
df1.insert(2,"Age",[17,18,20])
#print(df1)
del df1["Adress"]
#print(df1)
#dropping a column with pop
df2=df1.pop("Age")
print(df1)
print(df2)
