import subprocess
import re

class Process:
    """
    A class that represents a process.

    Methods:
        shell(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, regex_filter=None): 
            Executes a shell command and prints the output.
    """

    def __init__(self):
        pass

    @staticmethod
    def shell(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, regex_filter=None):
        """
        Executes a shell command and prints the output.

        Args:
            command (str): The shell command to execute.
            stdout (subprocess.PIPE, optional): The standard output stream. Defaults to subprocess.PIPE.
            stderr (subprocess.PIPE, optional): The standard error stream. Defaults to subprocess.PIPE.
            regex_filter (str, optional): A regular expression pattern to filter the output. Defaults to None.

        Returns:
            int: The return code of the process.
        """
        process = subprocess.Popen(command, shell=True, stdout=stdout, stderr=stderr, universal_newlines=True)
        
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                if regex_filter is not None:
                    pattern = re.compile(regex_filter)
                    match = re.search(pattern, output)
                    if match:
                        print(match.group())
                else:
                    print(output.strip())
        rc = process.poll()
        return rc
