import pandas as pd
import numpy as np
#creating dataframe by using dictionary
npar=np.array([['amit','aryan','anshu'],
              [102,103,104],[78,67,90]])
np_dict={'Names':npar[0],'Rollno':npar[1],'Marks':npar[2]}
df=pd.DataFrame(np_dict)
print(df)
