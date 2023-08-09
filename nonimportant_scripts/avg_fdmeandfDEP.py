# %%
import pandas as pd
import glob 
import os
# %%
files = sorted(glob.glob('/Users/owencollins/Desktop/summer_RA/data/fdmean/fdmean_sub*.tsv'))
data = []
# %%
for file in files:
    df = pd.read_csv(file, delimiter='\t')
    sub = df['sub'][0]  
    avg_fd_mean = df['fd_mean'].mean() 
    data.append({'sub': sub, 'avg_fd_mean': avg_fd_mean})

df_result = pd.DataFrame(data)
# %%
