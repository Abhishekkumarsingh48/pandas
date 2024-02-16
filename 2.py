#creatig a series by using array
import pandas as pd
import numpy as np
data=np.array([5,6,7,8])
print(data)
s=pd.Series(data)
print(s)
s1=pd.Series(data,index=[10,20,30,40])
print(s1)
