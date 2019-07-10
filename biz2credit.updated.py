

import pandas as pd
import numpy as np
data = pd.read_csv('C:/Users/3442/Desktop/cust.txt')
df=pd.DataFrame(data)
df
list(data.columns.values)
df.iloc[:,1:3]


