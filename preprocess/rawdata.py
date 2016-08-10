# -*- coding: cp949 -*-

__author__ = 'SungJoonPark'
import pandas as pd
import xlrd
import os


def preprocess_rawdata0623(inputfile,outputdir):
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    df = pd.read_excel(inputfile,sheetname=None,header=None,skiprows=4,index_col=0)
    #print df
    for sheet in df.keys():
        sheet_dir = outputdir+"/"+sheet
        if not os.path.exists(sheet_dir):
            os.makedirs(sheet_dir)
        df[sheet] = df[sheet].rename(index={'E2f(1)':'E2F1'})
        for i in range(0,60,3):
            outputfile=sheet_dir+"/"+str((i/3)+1)+".csv"
            df[sheet].iloc[:,i:i+3].T.to_csv(outputfile,index=False)



if __name__ == '__main__':
    rawdata0623_file = "Q:/LCA/data/raw data/drug_data_0623_fillblanck_with_day3.xlsx"
    outputdir = "./temp"
    preprocess_rawdata0623(rawdata0623_file,outputdir)