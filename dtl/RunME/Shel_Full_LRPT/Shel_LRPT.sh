#!/bin/bash
#
# CREATED USING THE BIOHPC PORTAL on Thu Mar 10 2022 15:55:23 GMT-0600 (Central Standard Time)
#
# This file is batch script used to run commands on the BioHPC cluster.
# The script is submitted to the cluster using the SLURM `sbatch` command.
# Lines starting with # are comments, and will not be run.
# Lines starting with #SBATCH specify options for the scheduler.
# Lines that do not start with # or #SBATCH are commands that will run.

# Name for the job that will be visible in the job queue and accounting tools.
#SBATCH --job-name ShelLRPT

# Name of the SLURM partition that this job should run on.
#SBATCH -p GPU       # partition (queue)
# Number of nodes required to run this job
#SBATCH -N 1

# Number of tasks 

# Time limit for the job in the format Days-H:M:S
# A job that reaches its time limit will be cancelled.
# Specify an accurate time limit for efficient scheduling so your job runs promptly.
#SBATCH -t 1-0:0:00

# The standard output and errors from commands will be written to these files.
# %j in the filename will be replace with the job number when it is submitted.

#SBATCH -o job_ShelLRPT_%j.out
#SBATCH -e job_ShelLRPT_%j.err

# Send an email when the job status changes, to the specfied address.
#SBATCH --mail-type FAIL
#SBATCH --mail-user yiqing.wang@utsouthwestern.edu


#SBATCH --array=6-10


###  

python Shel_LRPT.py 0 $SLURM_ARRAY_TASK_ID 



# END OF SCRIPT

