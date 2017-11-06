"""
Script for concatenating multiple CSV files into a single CSV file
"""

import os
import glob
import pandas as pd
import numpy as np


class obtain_samples:

      # def mergeCSV(path="/Users/seunghalee/Documents/git/CIS519/data/Trial1", outfile="/data/Trial1/Trial1.csv"):
        def __init__(self):
           '''

           '''


        def getpath(self,folder_name):

            '''
            :param folder_name: This is the folder that contains all the files
            :return: a list that contains all the csv file path
            '''

            if folder_name == "":
                return []
            #p = p.replace("/", "\\")
            if folder_name[-1] != '/':
                folder_name = folder_name + '/'

            sub_folder = os.listdir(folder_name)
            trial_number = np.size(sub_folder)
            file_path = []

            for i in np.arange(trial_number):
                file_path.append(glob.glob(os.path.join(folder_name+'/'+sub_folder[i],"*.csv")))

            return file_path



        def samples(self):

            '''
            Here we use the path that we generate in the pre
            :return:
            '''

            '''
                path = "data/Trial1"
                outfile = "data/Trial1/Trial1.csv"
                all_files = glob.glob(os.path.join(path, "*.csv"))
                df_from_each_file = (pd.read_csv(f) for f in all_files)
                concatenated_df = pd.concat(df_from_each_file, ignore_index=True)
                concatenated_df.to_csv(outfile,index=None)
        
                for i in np.arange[4]:
                    for j in np.arange[10]:
                        list[i,j] = csv.reader(f) in all_files
                        
            '''