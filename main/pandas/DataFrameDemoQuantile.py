import pandas as pd
import numpy as np

df = pd.DataFrame({'value': [1, 2, 3, 4, 5, 6, 7, 8,9,10],'name':[11,22,33,44,55,66,77,88,99,1010]},
                  index=['a','b','c','d','e','f','g','h','i','j'])

#print(df.value.quantile(0.9))
s = df[(np.array(df.value) == 8)|(np.array(df.name)== 1010) ]

s = b'\xe6\xa0\xa1\xe9\xaa\x8c\xe9\x80\x9a\xe8\xbf\x87'
str = s.decode('utf8')
print(str)

df.value.apply(lambda e: e+1 if(e>3) else e+2)