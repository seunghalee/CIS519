"""
Script for concatenating multiple CSV files into a single CSV file
"""

import os
import glob
import pandas as pd

# def mergeCSV(path="/Users/seunghalee/Documents/git/CIS519/data/Trial1", outfile="/data/Trial1/Trial1.csv"):
path = "/Users/seunghalee/Documents/git/CIS519/data/Trial1"
outfile = "/Users/seunghalee/Documents/git/CIS519/data/Trial1/Trial1.csv"
all_files = glob.glob(os.path.join(path, "*.csv"))
df_from_each_file = (pd.read_csv(f) for f in all_files)
concatenated_df = pd.concat(df_from_each_file, ignore_index=True)
concatenated_df.to_csv(outfile,index=None)