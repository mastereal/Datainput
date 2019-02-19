import os
import re
import pandas as pd
from pandas import DataFrame, Series

def pn(df,datatype,outdir,pntype="pro",Y=[],Pro=[],Pre=[],Fre=[],province=""):
    if Y!=[] or Pro!=[] or Pre!= [] or Fre!=[]:
        Y=[]
        Pro=[]
        Pre=[]
        Fre=[]
    print(Y)
    data_columns=list(df.columns.str.strip())
    print(data_columns)
    data_index=list(df.index)     
            #print(data_index)
            # 获取表格的列表
    if pntype=="pro":
        for y in data_index:
            for p in data_columns:                    
                f=df.loc[y,p]
                Y.append(y)
                Pro.append(p)
                Fre.append(f)
        pro_e_dic={"Year":Y,"Province":Pro,datatype:Fre}
        pro_etype=DataFrame(pro_e_dic,columns=["Year","Province",datatype])        
        filepath_fin=outdir+datatype+".xlsx"
        pro_etype.to_excel(filepath_fin)
    else:
        data_columns=list(df.columns.str.strip())
            #print(data_columns)
        data_index=list(df.index)     
            #print(data_index)
            # 获取表格的列表
        for y in data_index:
            for p in data_columns:                    
                f=df.loc[y,p]
                Y.append(y)
                Pre.append(p)
                Pro.append(province)
                Fre.append(f)
                    #print(Year)
                    #print(Province)
                    #print(Frequency) 
                #某一年当前省某一类
            #所有年当前省某一类
            #print(Year)
            #print(Prefecture)
            #print(Frequency)
        pre_e_dic={"Year":Y,"Province":Pro,"Prefecture":Pre,datatype:Fre}
        pre_etype=DataFrame(pre_e_dic,columns=["Year","Province","Prefecture",datatype])        
        filepath_fin=outdir+datatype+".xlsx"
        pre_etype.to_excel(filepath_fin)
    #所有年所有省某一类
    #print(Year)
    #print(Prefecture)
    #print(Frequency)
   

pop_data=pd.read_excel("po-fa.xlsx",header=0,sheet_name="Population",index_col=0)
farm_data=pd.read_excel("po-fa.xlsx",header=0,sheet_name="Farmland",index_col=0)
for pro in list(pop_data.columns.str.strip()):  
    pop_data[pro]=pop_data[pro].interpolate(method="linear")
for pro in list(farm_data.columns.str.strip()):
    farm_data[pro]=farm_data[pro].interpolate(method="linear")
pop_data.to_excel("pro_pop.xlsx")
farm_data.to_excel("pro_farm.xlsx")
#pop_df=pd.read_excel("pro_pop.xlsx",header=0,sheet_name=0,index_col=0) # Need edit
#farm_df=pd.read_excel("pro_farm.xlsx",header=0,sheet_name=0,index_col=0)
#pn(pop_df,"Population","./Propanelise/")
#pn(farm_df,"Farmland","./Propanelise/")
tax_food=pd.read_excel("po-fa.xlsx",header=0,sheet_name="AgricultureTax_food",index_col=0)
tax_currency=pd.read_excel("po-fa.xlsx",header=0,sheet_name="AgricultureTax",index_col=0)
for pro in list(tax_food.columns.str.strip()):  
    tax_food[pro]=tax_food[pro].interpolate(method="linear")
for pro in list(tax_currency.columns.str.strip()):
    tax_currency[pro]=tax_currency[pro].interpolate(method="linear")
tax_food.to_excel("pro_taxf.xlsx")
tax_currency.to_excel("pro_taxc.xlsx")