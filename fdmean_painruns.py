# load .tsv as pandas
# grab column name: framewise_displacement
# average value of fd. np.mean()
# use .at and save in new dataframe
# %%
# /dartfs-hpc/rc/lab/C/CANlab/labdata/data/spacetop_data/derivatives/fmriprep/results/fmriprep/sub-0071/ses-01/func
import numpy as np
import pandas as pd
import os
import glob
from os.path import join
# %%
fname = "/Users/owencollins/Desktop/summer_RA/data/sub-0071_ses-01_task-social_acq-mb8_run-6_desc-confounds_timeseries.tsv"
fmridf = pd.read_csv(fname, sep = '\t')
# %%
fmridf.columns
# %%
subset_fmridf = fmridf[["framewise_displacement"]]
# %%
subset_fmridf.mean(axis=0)
data = subset_fmridf["framewise_displacement"].mean(axis=0)
# %%
meandf = pd.DataFrame(columns=['sub', 'ses', 'run', 'fd_mean'], index = (0,1))
meandf.loc[0:1,'fd_mean',] = data
# %%
