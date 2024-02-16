import pandas as pd
a=[12,13,14,15]
x=pd.Series(a)
print(x)
y=[13,'As',23,'ram']
s1=pd.Series(y)
print(s1)
print(s1[3])
#own index value
s2=pd.Series(y,index=['x','y','z','p'])
print(s2)
print(s2['y'])
