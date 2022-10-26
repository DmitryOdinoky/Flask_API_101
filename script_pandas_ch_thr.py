
import os
# import time

import concurrent.futures
import multiprocessing

import pandas as pd

num_processes = multiprocessing.cpu_count()

my_absolute_dirpath = os.getcwd()
my_absolute_dirpath.replace('\\' ,'/')
my_absolute_dirpath = my_absolute_dirpath.replace('\\' ,'/')



def process_csv(filename):

    

    df_iter = pd.read_csv(my_absolute_dirpath + "/input/" + filename, index_col=False, chunksize=500)
    
    for i, df_out in enumerate(df_iter):
        
        with concurrent.futures.ProcessPoolExecutor(num_processes) as pool:
    
    
            df_out = df_out.groupby(["Song", "Date"])["Number of Plays"].sum().reset_index().sort_values(by=['Song'], ascending=False) 
    
            pool.submit(df_out.to_csv, my_absolute_dirpath + "/output/" + filename)

    





