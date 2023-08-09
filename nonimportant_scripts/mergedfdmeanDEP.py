# %%
import pandas as pd
import glob
#%%
file_paths = sorted(glob.glob('/Users/owencollins/Desktop/summer_RA/data/fdmean/fdmean_sub*.tsv'))
data_frames = []
#%%
for file_path in file_paths:
    df = pd.read_csv(file_path, sep='\t')
    data_frames.append(df)
#%%
merged_data = pd.concat(data_frames, ignore_index=True)
#%%
merged_data.to_csv('/Users/owencollins/Desktop/mergedfdmean.tsv', sep='\t', index=False)


# %%
