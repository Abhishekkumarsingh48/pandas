import pandas as pd
import numpy as np
#creating dataframe by using list of dictionary
x=[{"name":"amit","roll":3,"marks":91},
            {"name":"abhi","roll":4,"marks":92},
            {"name":"ravi","roll":5,"marks":93},
            {"name":"ram","roll":6,"marks":94}]
df=pd.DataFrame(x)
print(df)
            

