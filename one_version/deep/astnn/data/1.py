import pandas as pd
import numpy as np

projects=['ambari','ant','argouml','hibernate','jenkins','jmeter','lucene','poi_3.1']
# projects=['ambari']
for project in projects:
    path=project+'/programs.pkl'
    data=pd.read_pickle(path)
    label=data['label'].values
    print('sample=',len(label), '  ', 'change rate=',sum(label)/len(label))