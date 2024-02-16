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
#rename
df1.rename(columns={"name":"Student_name"},inplace=True)
print(df1)
#df1.to_csv(r"C:\Users\Admin\Documents\New folder")
df=pd.read_csv(r"C:\Users\Admin\Documents\New folder")
print(df)
print(df.roll.count())
print(df.marks.sum())
print("Max Marks",df.marks.max())
print("Min Marks",df.marks.min())
