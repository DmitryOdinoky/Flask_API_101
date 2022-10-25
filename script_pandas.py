
import os
import time

import pandas as pd


my_absolute_dirpath = os.getcwd()
my_absolute_dirpath.replace('\\' ,'/')
my_absolute_dirpath = my_absolute_dirpath.replace('\\' ,'/')



def process_csv(filename):
    
    st = time.time()
    


    df = pd.read_csv(my_absolute_dirpath + "/input/" + filename, index_col=False)
    df_out = df.groupby(["Song", "Date"])["Number of Plays"].sum().reset_index().sort_values(by=['Song'], ascending=False) 

    df_out.to_csv(my_absolute_dirpath + "/output/" + filename, index=False)
    
    et = time.time()
    elapsed_time = round(et - st, 6)





