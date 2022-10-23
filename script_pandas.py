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

    df = pd.read_csv(my_absolute_dirpath + "/input/" + filename, index_col=False)
    df_out = df.groupby(["Song", "Date"])["Number of Plays"].sum().reset_index().sort_values(by=['Song'], ascending=False) 
    # output_file = filename
    df_out.to_csv(my_absolute_dirpath + "/output/" + filename, index=False)
    
    et = time.time()
    elapsed_time = round(et - st, 2)

    return filename, elapsed_time



#o_file = process_csv("D:/SW/-=Python projects=-/flask_api_101/Flask_API_101/assets/data/test_1.csv")