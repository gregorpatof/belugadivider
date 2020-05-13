#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --exclusive
#SBATCH --mem=0
#SBATCH --time=3:00:00
#SBATCH --account=rrg-najmanov
module load python/3
