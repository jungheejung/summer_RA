# %% libraries
import numpy as np
import pandas as pd
import os
import glob
from os.path import join

sub = 'sub-0029'
main_dir = '/Users/h/Documents/summer/summer_RA'

# %% 
# 1. glob all files in 'data' directory
fname_pattern = os.path.join(main_dir, 'data', f'*_beh.csv')
flist = glob.glob(fname_pattern)
for fname in flist:
    print(fname)

    behdf = pd.read_csv(fname)
    behdf.head()
    behdf.columns.tolist()[0] 
    
    # TODO: change this ndarfname into a relative path using `main_dir`
    ndarfname = '/Users/h/Documents/summer/summer_RA/resources/ndar_subject.csv'
    summerdf = pd.read_csv(ndarfname)

    # 2. find the corresponding subject key
    # from that, extract all the essential columns

    subset_summer = summerdf[summerdf['src_subject_id'] == sub][[ 'subjectkey', 'src_subject_id',  'sex',
              'race', 'ethnic_group', 'phenotype', 'phenotype_description',
              'twins_study', 'sibling_study', 'family_study', 'interview_date',
              'interview_age']]
    
    ## DEP: masking a dataframe
    # condition_of_interest = summerdf['src_subject_id'] == 'sub-0029'
    # summerdf * condition_of_interest

    subset_summer_repeat = pd.concat([subset_summer]*len(behdf), ignore_index= True )
    merge_df = pd.concat([subset_summer_repeat, behdf], axis = 1)

    # save pandas as csv
    # TODO: declare a save_dir instead of an absolute path like '/Users/h/Desktop'
    save_fname = join('/Users/h/Desktop', os.path.basename(fname)[:-4] + '_NDA.csv')
    merge_df.to_csv(save_fname)

# %%
