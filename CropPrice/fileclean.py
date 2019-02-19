import os
import re
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import csv

filelist=os.listdir("./")
for filename in filelist:
    if re.search(".csv",filename)!=None:
        csvfile=open(filename,encoding="utf-8-sig")
        #try:
            #print(csvfile) 
        csvfile_lines=csv.reader(csvfile)
        print(csvfile_lines)
        ori_data_list=[]
        for lines in csvfile_lines:
            ori_data_list.append(lines)
        if ori_data_list==[]:

            
        #except:
            #os.remove(filename)
            print(filename)
        else:
            ori_data_before_1=pd.DataFrame(ori_data_list)
            if len(list(ori_data_before_1.columns))==28:
                ori_data_before=ori_data_before_1.drop(columns=[27])
            else:    
                ori_data_before=ori_data_before_1
            ori_data_after=ori_data_before.fillna("") #处理 None
            ori_data=ori_data_after.replace("",np.nan)
            #print(ori_data_after)
            print(ori_data)
            
            aver_array_str=ori_data.iloc[2:,3:]
            aver_array=aver_array_str.convert_objects(convert_numeric=True)
            print(aver_array)
            averprice=aver_array.mean(1)
            print(averprice)
            #print(ori_data)
            Year=ori_data.loc[2:,2]
            #print(Year)
            check=re.match("([A-Z][A-Z])_all_([A-Z][A-Z0-9]).csv",filename)
            Provincename=check.group(1)
            Grain=check.group(2)
            df_dict={"Year":Year,Grain:averprice}
            df=pd.DataFrame(df_dict,columns=["Year",Grain])
            df["Province"]=Provincename
            filename_after="./Afterclean/"+Provincename+"_"+Grain+".xlsx"
            print(df)
            df.to_excel(filename_after)