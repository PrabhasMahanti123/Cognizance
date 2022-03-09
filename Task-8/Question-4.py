import pandas as pd
ser = pd.Series(['Data', 'science', 'Machine', 'learning', 'Artificial', 'intelligence'])
for i in ser:
    v = i
    k = v.capitalize()
    print(k , end = " ")
