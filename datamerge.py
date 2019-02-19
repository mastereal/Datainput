import os
import re
import pandas as pd
from pandas import DataFrame, Series

oridata=pd.read_excel("./Propanelise/Population.xlsx",header=0,sheet_name=0,index_col=0)
merge1=pd.read_excel("./Propanelise/Farmland.xlsx",header=0,sheet_name=0,index_col=0)
result=pd.merge(oridata,merge1,on=["Year","Province"])
filelist=os.listdir("./Environment/Panelise/")
for filename in filelist:
    if re.match("Pro",filename)!=None:
        filepath="./Environment/Panelise/"+filename
        merge=pd.read_excel(filepath,header=0,sheet_name=0,index_col=0)
        result=pd.merge(result,merge,on=["Year","Province"])
e_typelist=["drought","flood","freeze","wind"]
for e_type in e_typelist:
    e_type_d=e_type+"_D"
    result[e_type_d]=""
    for i in list(result.index):
        if result.loc[i,e_type]==0:
            result.loc[i,e_type_d]=0
        else:
            result.loc[i,e_type_d]=1
print(result)
result.to_excel("./Propanelise/All.xlsx")