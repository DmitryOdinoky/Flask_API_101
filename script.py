import csv
import os

from collections import defaultdict
from datetime import datetime
from decimal import Decimal

my_absolute_dirpath = os.getcwd()
my_absolute_dirpath.replace('\\' ,'/')
my_absolute_dirpath = my_absolute_dirpath.replace('\\' ,'/')

#%%
def process_csv(filename):
    product_types = defaultdict(Decimal)

    with open(filename, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                hypen_idx = row['product'].replace('"', '').split().index('-')
                product_type =  ' '.join(row['product'].split()[:hypen_idx])
                product_types[product_type] += Decimal(row['price'][1:])
            except ValueError:
                product_types[row['product'].replace('"', '')] += Decimal(row['price'][1:])

    output_file = "data_temp_out.csv"
    
    with open(my_absolute_dirpath + "/output/" + output_file , 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['product_type', 'price'])

        for product_type, price in product_types.items():
            writer.writerow([product_type, price])

    return output_file