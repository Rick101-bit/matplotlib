import pandas as pd
#ds= pd.read_csv("D:\PYTHON\kohli_ipl.csv")
de= pd.read_csv("D:\PYTHON\pandas\csvdata\datasets-session-16\subs.csv")
print(de)
vk =pd.read_csv("D:\PYTHON\pandas\csvdata\datasets-session-16\kohli_ipl.csv",index_col="match_no").squeeze()
print(vk)
print((type(vk)))
print(vk.head(3))