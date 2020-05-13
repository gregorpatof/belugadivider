# Beluga Divider

These two Python scripts are used to divide a number of commands, supplied as a text file with one command per line, between a number of nodes on Beluga. It does so automatically.

First, the beluga_divider.py script will generate the jobs:

python beluga_divider.py /absolute/path/to/commands.txt n_nodes job_header.sh jobs_directory /absolute/path/working_directory

As you can see, it takes 5 arguments:

1. The commands file, in absolute path
2. The number of nodes to use
3. A job header (a default one is supplied in this git, but the time should be changed to match the user's needs)
4. The directory in which the jobs will be created (no absolute path needed)
5. The working directory for all the jobs, absolute path

That is all! Once this script has been run, the generated jobs will be found in the supplied jobs_directory, number from 0 to n-1. The jobs can be started individually with sbatch, or all at once by calling the generated bash script start_jobs.sh, also in the jobs_directory.
