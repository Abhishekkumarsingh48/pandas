#creating series by using a particular value
import pandas as pd
import numpy as np
s=pd.Series(10,index=[1,2,3,4,5])
print(s)
s1=pd.Series(np.ones(10))
print(s1)
s2=pd.Series(np.zeros(4))
print(s2)
s3=pd.Series(np.arange(12,24,2))
print(s3)
