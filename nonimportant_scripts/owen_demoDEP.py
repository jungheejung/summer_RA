# %%
from nilearn import image, plotting, masking, maskers
import os, glob, re 
import pandas as pd 
import numpy as np
from os.path import join

# %%
canlab_dir = '/Users/h/Documents/MATLAB/CanlabCore'
mask_fname = join(canlab_dir, 'CanlabCore/canlab_canonical_brains/Canonical_brains_surfaces/brainmask_canlab.nii.gz')
brain_mask = image.load_img(mask_fname)
plotting.plot_stat_map(brain_mask, display_mode='mosaic')

# %% mask
threshold = 0.5
clean_mask = masking.compute_epi_mask(image.load_img(mask_fname), 
                         lower_cutoff=threshold, 
                         upper_cutoff=.9)
plotting.plot_stat_map(clean_mask)

# %%
func = image.load_img('/Users/h/Documents/projects_local/sandbox/sub-0009/ses-04/func/sub-0009_ses-04_task-fractional_acq-mb8_run-2_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz')
plotting.plot_stat_map(image.index_img(func, 100))

# %%
# plotting.plot_stat_map(func, bg_img=clean_mask)
plotting.plot_stat_map(image.mean_img(func),
                       #image.index_img(func, 300),
                       cut_coords=(0,0,0), 
                       draw_cross=False,
                       black_bg=True)
# %%
nifti_masker = maskers.NiftiMasker(mask_img= masking.compute_epi_mask(image.load_img(mask_fname), lower_cutoff=threshold, upper_cutoff=1.0),
                            # target_affine = ref_img.affine, target_shape = ref_img.shape, 
                    memory="nilearn_cache", memory_level=1)

mask_arr = nifti_masker.fit_transform(image.mean_img(func))
masked_nii = nifti_masker.inverse_transform(mask_arr)
# %%
