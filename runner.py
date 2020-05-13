from multiprocessing import Pool
import sys
import subprocess
import shlex
from itertools import repeat


def execute(command_string, working_directory=None, capture_output=True):
    """ This function executes a system command that is passed as a string. It returns a CompletedProcess instance
        ( see https://docs.python.org/3/library/subprocess.html#subprocess.run for more info).
        The working directory can be set with the optional argument working_directory, otherwise it will be the
        current directory. By default the output (stdout and stderr) is captured.
    """
    assert isinstance(command_string, str)
    commands_list = shlex.split(command_string)  # the command needs to be a list for subprocess.run()
    if capture_output:
        return subprocess.run(commands_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=working_directory)
    else:
        return subprocess.run(commands_list, cwd=working_directory)


def run_list(commands_list, working_directory, capture_output=True, n_processors=40):
    p = Pool(n_processors)
    p.starmap(execute, zip(commands_list, repeat(working_directory), repeat(capture_output)))


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise ValueError("I need 4 args: the commands list file, the start index, the stop index and the working directory")
    commands_file = sys.argv[1]
    start_i = int(sys.argv[2])
    stop_i = int(sys.argv[3])
    work_dir = sys.argv[4]
    with open(commands_file) as f:
        lines = [x.strip() for x in f.readlines()]
        lines = [line for line in lines if len(line) > 0]
        lines = lines[start_i:stop_i]
    run_list(lines, work_dir)
