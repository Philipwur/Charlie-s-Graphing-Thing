# -*- coding: utf-8 -*-
"""
steps
1. delete descriptions and unmerge cells in excel file
2. save excel file as CSV UTF-8 into the target directory
3. change filename variable below to the file you want to read/plot
4. run the code!

note
there seems to be a glitch where when converting from excel a bunch of empty 
columns are created. Added a bit where these are removed from the dataframe.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_name = "A01044_2.csv"

"""
make pandas only read the appropriately titled columns
make linegraph
normalise data
impose multiple linegraphs on top of eachother (add 1 to normalised data)
colours + legend

check data formatter (3 formats)
"""

df = pd.read_csv(file_name, sep=",", encoding="utf-8")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

print(df)

#%%

"""
plotting component
"""

plt.figure()
fig1 = sns.pairplot(df, size = 2.5, diag_kind="kde")
fig1.fig.suptitle('Title of Plot',y=1.04)

plt.figure(figsize=(10, 5))
fig2 = sns.lineplot(data=df, x="2θ (°)", y="I (count)")
fig2.set(title='Title of Plot')
fig2.sns.axes_style('white')