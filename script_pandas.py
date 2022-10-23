# import csv
import os
import time

import pandas as pd


my_absolute_dirpath = os.getcwd()
my_absolute_dirpath.replace('\\' ,'/')
my_absolute_dirpath = my_absolute_dirpath.replace('\\' ,'/')

st = time.time()

def process_csv(filename):
    

    
        
    df_iter = pd.read_csv(my_absolute_dirpath + "/input/" + filename, index_col=False, chunksize=500)
    
    for i, df_out in enumerate(df_iter):
    
        df_out = df_out.groupby(["Song", "Date"])["Number of Plays"].sum().reset_index().sort_values(by=['Song'], ascending=False) 
     
        # Set writing mode to append after first chunk
        mode = 'w' if i == 0 else 'a'
        
        # Add header if it is the first chunk
        header = i == 0
        
        df_out.to_csv(my_absolute_dirpath + "/output/" + filename, index=False, header=header, mode=mode)
    
    
    et = time.time()
    elapsed_time = round(et - st, 2)

    return filename, elapsed_time



