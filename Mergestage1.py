import os
import re
import pandas as pd
from pandas import DataFrame, Series

#price_data=pd.read_excel("Pro_R1_None.xlsx",header=0,index_col=0)

#for pro in list(price_data.columns.str.strip()):  
    #price_data[pro]=price_data[pro].interpolate(method="linear")
#price_data.to_excel("pro_price.xlsx")
oridata=pd.read_excel("./Propanelise/AgricultureTax.xlsx",header=0,sheet_name=0,index_col=0)
#oridata=pd.read_excel("./Propanelise/UrbantoRural.xlsx",header=0,sheet_name=0,index_col=0)
merge1=pd.read_excel("./Propanelise/All.xlsx",header=0,sheet_name=0,index_col=0)
result=pd.merge(oridata,merge1,on=["Year","Province"])
result.to_excel("./Propanelise/All.xlsx")
