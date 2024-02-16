#creating a DF using random function
import pandas as pd
import numpy as np
df=pd.DataFrame(np.random.rand(200,5))
print(df)
print(df.head(7))
print(df.tail(3))
print(df.to_string())
df1=pd.DataFrame(np.random.randint(2,8,size=(5,6)))
print(df1)
