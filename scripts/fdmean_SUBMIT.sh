#!/bin/bash -l
#SBATCH --job-name=fdmean
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --mem-per-cpu=20G
#SBATCH --time=02:00:00
#SBATCH -o ./logplot/GLM_%A_%a.o
#SBATCH -e ./logplot/GLM_%A_%a.e
#SBATCH --account=DBIC
#SBATCH --partition=standard
#SBATCH --array=4%10

conda activate spacetop_env
echo "SLURMSARRAY: " ${SLURM_ARRAY_TASK_ID}
ID=$((SLURM_ARRAY_TASK_ID-1))
MAINDIR='/dartfs-hpc/rc/lab/C/CANlab/labdata/projects/spacetop_projects_cue'
NPYDIR='/dartfs-hpc/rc/lab/C/CANlab/labdata/data/spacetop_data/derivatives/fmriprep_qc/numpy_bold'
OUTPUTDIR="/dartfs-hpc/rc/lab/C/CANlab/labdata/data/spacetop_data/derivatives/fmriprep_qc/fmriprep_bold_correlation"

python ${MAINDIR}/scripts/step00_qc/qc03_fmriprep_visualize/qc05_plotfmriprep.py \
--slurm-id ${ID} \
--fmriprepdir ${NPYDIR} \
--savedir ${OUTPUTDIR}
