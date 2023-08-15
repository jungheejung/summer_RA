# Summer_RA
*This document outlines important information regarding the Summer_RA folder. This folder was created by Heejung and Owen.*

## Details:
* The `data` sub-folder contains various .tsv files and important data

* The `nonimportant_sripts` sub-folder contains scripts that were used for data analysis, however, aren't necessary for gathering or runing data

* The `scripts` sub-folder contains useful scripts for plotting and data analysis as well as SLURM scripts

## Codes:
* `scripts/fd_mean_spacetop.py` is a generic code to be able to gather data from the Discovery Cluster. *needs to be run with `SLURM_task.sh` (found under `scripts`)

* `R_tasks_dvars.Rmd` and `R_tasks_globalsignal.Rmd` are useful codes to create raincloud plots (found under `scripts`)

* `mergedfdmeandfDEP.py` is useful for merging many .tsv files to one data frame. *you will need to change paths for data and where to save (found under `nonimportant_sripts`) 
