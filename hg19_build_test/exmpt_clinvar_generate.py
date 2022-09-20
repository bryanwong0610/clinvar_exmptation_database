import pandas as pd
import numpy as np
import os
from pandas import value_counts

clinvar_test = pd.read_table("/mnt/datashare/home/wangzesong/clinvar/hg19_build/GRCh37_clinvar_20220719.txt")
CLIN_exmpt=[]
CLIN_exmpt=clinvar_test['CLNSIG'].str.contains('genic')
CLIN_exmpt.value_counts()
clinvar_test['CLIN_exmpt'] = CLIN_exmpt
final_clinvar=clinvar_test[['#Chr','Start','End','Ref','Alt','GENEINFO','CLNALLELEID','CLNDN','CLNDISDB','CLNHGVS','CLNSIG','CLNREVSTAT','CLIN_exmpt']]
final_clinvar.to_csv('/mnt/datashare/home/wangzesong/clinvar/hg19_build/hg19_clinvar_exmpt.txt',sep='\t',index=False)
