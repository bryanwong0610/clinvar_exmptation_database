import pandas as pd
import numpy as np
import os
from pandas import value_counts
import argparse
# read file & argument set up 

def argument_get():
    parser=argparse.ArgumentParser(prog='Clinvar database exmptation',description='A python script for generate clinvar database')
    parser.add_argument('--Input','-i',type=str,help='raw clinvar data')
    args,_ = parser.parse_known_args()
    args = vars(args)
    print(args) #test
    return args
args= argument_get()
file_name= './'+args['Input']+'.txt'
clinvar_test = pd.read_table(file_name)
CLIN_exmpt=[]
CLIN_exmpt=clinvar_test['CLNSIG'].str.contains('genic')
CLIN_exmpt.value_counts()
clinvar_test['CLIN_exmpt'] = CLIN_exmpt
final_clinvar=clinvar_test[['#Chr','Start','End','Ref','Alt','GENEINFO','CLNALLELEID','CLNDN','CLNDISDB','CLNHGVS','CLNSIG','CLNREVSTAT','CLIN_exmpt']]
if 'GRCh38' in file_name:
    ver='hg38'
elif 'GRCh37' in file_name:
    ver='hg19'
result_name='./'+ver+'_clinvar_exmpt.txt'
final_clinvar.to_csv(result_name,sep='\t',index=False)
