# %% libraries
import numpy as np
import pandas as pd
import os

sub = 'sub-0029'
main_dir = '/Users/h/Documents/summer/summer_RA'
# %% comment
fname = os.path.join(main_dir, 'data', f'{sub}_ses-01_task-social_run-01-vicarious_beh.csv')
behdf = pd.read_csv(fname)
behdf.head()
behdf.columns.tolist()[0] 
# %%
ndarfname = '/Users/h/Documents/summer/summer_RA/resources/ndar_subject.csv'
summerdf = pd.read_csv(ndarfname)
# %%
# goal: sub-0029, find the corresponding subject key
# from that, extract all the essential columns
# condition_of_interest = summerdf['src_subject_id'] == 'sub-0029'
# summerdf * condition_of_interest
subset_summer = summerdf[summerdf['src_subject_id'] == sub][[ 'subjectkey', 'src_subject_id',  'sex',
       'race', 'ethnic_group', 'phenotype', 'phenotype_description',
       'twins_study', 'sibling_study', 'family_study', 'interview_date',
       'interview_age']]
# %%
subset_summer_repeat = pd.concat([subset_summer]*len(behdf), ignore_index= True )
merge_df = pd.concat([subset_summer_repeat, behdf], axis = 1)
# %%
