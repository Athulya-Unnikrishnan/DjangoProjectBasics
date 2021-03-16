import pandas as pd

data={'Name':['aromal','kini','aghori','athulya'],
      'Age':[24,23,23,24]}

df=pd.DataFrame(data)
print(df.loc['aromal':'kini'])