import pandas as pd
import numpy as np
#creating dataframe by using list of list
x=np.array([['amit','aryan','anshu'],
              [102,103,104],[78,67,90]])
df=pd.DataFrame(x,index=['name','roll','marks'])
print(df)
