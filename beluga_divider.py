import sys
import os
import random


def shuffle_commands(commands_file):
    """ Shuffles the commands (for a more uniform computational load) and returns the number of commands.]
    """
    with open(commands_file) as f:
        lines = [x.strip() for x in f.readlines()]
        lines = [line for line in lines if len(line) > 0]
    random.shuffle(lines)  # better to shuffle the commands for uniform computational load
    with open(commands_file, 'w') as f:
        for line in lines:
            f.write(line + "\n")
    return len(lines)


def make_job(job_header, jobs_dir, start_i, stop_i, job_i, commands_file, runner_path, work_dir):
    with open(job_header) as f:
        lines = f.readlines()
    with open("{0}/job_{1}.sh".format(jobs_dir, job_i), "w") as f:
        for line in lines:
            f.write(line)
        f.write("{0} {1} {2} {3} {4}\n".format(runner_path, commands_file, start_i, stop_i, work_dir))


def write_job_starter(jobs_dir, n_jobs):
    with open("{0}/start_jobs.sh".format(jobs_dir), "w") as f:
        for i in range(n_jobs):
            f.write("sbatch job_{0}.sh\n".format(i))


def correct_folder(folder):
    if folder[-1] == "/":
        return folder[:-1]
    return folder


if __name__ == "__main__":
    if len(sys.argv) != 6:
        raise ValueError("I need 5 args: the file containing the list of commands, the number of nodes to use, " +
                         "the job file header, the directory where to put the jobs " +
                         "and the working directory for the jobs.")
    commands_file = sys.argv[1]
    n_nodes = int(sys.argv[2])
    job_header = sys.argv[3]
    jobs_dir = correct_folder(sys.argv[4])
    work_dir = correct_folder(sys.argv[5])
    dirpath = os.path.dirname(os.path.abspath(__file__))
    runner_path = "{0}/runner.py".format(dirpath)
    n = shuffle_commands(commands_file)
    step = n/n_nodes
    start_i_float = 0
    stop_i_float = None
    for j in range(n_nodes):
        stop_i_float = start_i_float + step
        make_job(job_header, jobs_dir, round(start_i_float), round(stop_i_float), j, commands_file, runner_path, work_dir)
        start_i_float = stop_i_float
    write_job_starter(jobs_dir, n_nodes)

