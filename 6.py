import pandas as pd
import numpy as np
#creating dataframe by using arrays
npar=np.array([['amit','aryan','anshu'],
              [102,103,102],[78,67,90]])
df=pd.DataFrame(npar,columns=['id1','id2','id3'],index=['name','Roll_No','Marks'])
print(df)
