import numpy as np
import pandas as pd

x = np.array([[1,2],[2,3]])
y = np.array([[1,5,4],[2,5,6]])


dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data)



exam = {

    'test1':[15,16,17],
    'test2':[16,25,15]
}

df = pd.DataFrame([[18, '남','김천고'], [19, '여', '울산고']],
                 index=['진현', '민지'],
                 columns=['나이', '성별', '학교'])

label1 = df.loc[['진현']]

print(label1)


# print(df)
# print(df.index)
# print(df.columns)


