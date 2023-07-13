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
from pathlib import Path
import re
# %%
current_dir = os.getcwd()
# main_dir = Path(current_dir).parents[1]
main_dir = current_dir
# %%
sub = 'sub-0002'
fmriprep_dir = '/dartfs-hpc/rc/lab/C/CANlab/labdata/data/spacetop_data/derivatives/fmriprep/results/fmriprep'
flist = sorted(glob.glob(join(fmriprep_dir, sub, '*', 'func', f'{sub}_*_task-social_acq-mb8_run-*_desc-confounds_timeseries.tsv'), recursive=True))
# "sub-0071_ses-01_task-social_acq-mb8_run-6_desc-confounds_timeseries.tsv"
# fname = join(main_dir, "/data/sub-0071_ses-01_task-social_acq-mb8_run-6_desc-confounds_timeseries.tsv")
meandf = pd.DataFrame(columns=['sub', 'ses', 'run', 'fd_mean'], index = range(len(flist)))
for ind, fpath in enumerate(sorted(flist)):
    fmridf = pd.read_csv(fpath, sep = '\t')
    # fmridf.columns
    subset_fmridf = fmridf[["framewise_displacement"]]
    # subset_fmridf.mean(axis=0)
    data = subset_fmridf["framewise_displacement"].mean(axis=0)
    meandf.loc[ind,'fd_mean'] = data
    match_sub = re.search(r"sub-(\d+)", fpath).group(1)
    match_ses = re.search(r"ses-(\d+)", fpath).group(1)  # Find the match in the filename
    match_run = re.search(r"run-(\d+)", fpath).group(1) 
    meandf.loc[ind,'sub'] = f"sub-{match_sub}"
    meandf.loc[ind,'ses'] = f"ses-{match_ses}"
    meandf.loc[ind,'run'] = f"run-{int(match_run):02d}"
# %%
save_dir = '/dartfs-hpc/rc/lab/C/CANlab/labdata/data/spacetop_data/derivatives/fmriprep_qc'
save_fname = join(save_dir, f"fdmean_{sub}.tsv")
meandf.to_csv(save_fname, sep='\t', index=False, header=True)