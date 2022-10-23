# import csv
import os
import time

import pandas as pd
# from collections import defaultdict
# from datetime import datetime
# from decimal import Decimal

my_absolute_dirpath = os.getcwd()
my_absolute_dirpath.replace('\\' ,'/')
my_absolute_dirpath = my_absolute_dirpath.replace('\\' ,'/')

st = time.time()

def process_csv(filename):
    
    # product_types = defaultdict(Decimal)
    
        
    df_iter = pd.read_csv(my_absolute_dirpath + "/input/" + filename, index_col=False, chunksize=500)
    
    for i, df_out in enumerate(df_iter):
    
        df_out = df_out.groupby(["Song", "Date"])["Number of Plays"].sum().reset_index().sort_values(by=['Song'], ascending=False) 
        # output_file = filename
        
        # Set writing mode to append after first chunk
        mode = 'w' if i == 0 else 'a'
        
        # Add header if it is the first chunk
        header = i == 0
        
        df_out.to_csv(my_absolute_dirpath + "/output/" + filename, index=False, header=header, mode=mode)
    
    
    et = time.time()
    elapsed_time = round(et - st, 2)

    return filename, elapsed_time



#o_file = process_csv("D:/SW/-=Python projects=-/flask_api_101/Flask_API_101/assets/data/test_1.csv")