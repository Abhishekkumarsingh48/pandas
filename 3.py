import pandas as pd
import numpy as np
dict = {'x':12,'y':14,'z':16}
s1=pd.Series(dict,index=['x','y','x','y',2,'z',1,'z'])
print(s1)
