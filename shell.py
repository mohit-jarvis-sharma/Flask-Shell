import shlex
import shutil
import os
import subprocess

def shell_result(my_cmd):
    my_cmd = shlex.split(my_cmd)
    result = func_call(my_cmd)
    return result

def func_call(my_cmd):
    temp_result = '-- '
    if my_cmd[0] == 'ls':
        for i in os.listdir(os.getcwd()):
            temp_result += i + ",   "
    elif my_cmd[0] == 'help':
        try:
            temp_result += 'cd = Takes one argument.Changes directory\n' \
                        + 'ls = Takes no arguments. Lists all files in the current directory\n' \
                        + 'mkdir = Takes one argument.Creates a new directory\n' \
                        + 'rm = Takes one argument.Removes the specified file\n' \
                        + 'details = Takes no argument.Returns a system\'s information\n' \
                        + 'rmdir = Takes one argument.Deletes folder.\n' \
                        + 'open = Takes two argument.Opens specified file using specified program if the program exists.\n' \
                        + 'misc = Takes multiple parameters.Executes command on the master terminal' \
                        + 'cp = Takes two arguments.Copies a file to a desired location' \
                        + 'ps = Display current active processes' 
        except:
            temp_result += 'Invalid syntax or Missing parameters.'
    elif my_cmd[0] == 'mkdir':
        try:
            if my_cmd[1] not in os.listdir(os.getcwd()):
                os.mkdir(my_cmd[1])
                temp_result += my_cmd[1] + ' created.'
            else:
                temp_result += 'Directory already exists'
        except:
            temp_result += 'Invalid syntax or Missing parameters.'
    elif my_cmd[0] == 'cd':
        try:
            if os.getcwd() != my_cmd[1]:
                os.chdir(my_cmd[1])
                temp_result += 'Directory changed.'
            else:
                temp_result += 'File Not Found or already in the directory'
        except:
            temp_result += 'Invalid syntax or Missing parameters'
    elif my_cmd[0] == 'rm':
        try:
            os.remove(my_cmd[1])
            temp_result += 'File ' + my_cmd[1] +' removed.'
        except:
            temp_result += 'Invalid syntax or Missing parameters'
    elif my_cmd[0] == 'details':
        try:
            for i in os.uname():
                temp_result += i + '   '
        except:
            temp_result += 'Invalid syntax or missing parameters'
    elif my_cmd[0] == 'rmdir':
        try:
            shutil.rmtree(my_cmd[1])
            temp_result += 'Folder ' + my_cmd[1] + ' deleted.'
        except:
            temp_result += 'Invalid syntax or missing parameters'
    elif my_cmd[0] == 'open':
        try:
            os.system(my_cmd[1] + ' ' + my_cmd[2])
            temp_result += 'Opening ' + my_cmd[2] + ' using ' + my_cmd[1]
        except:
            temp_result += 'Invalid syntax or missing parameters'
    elif my_cmd[0] == 'misc':
        try:
            temp_query = ''
            for i in range(1,len(my_cmd)):
                temp_query += my_cmd[i] + ' '
            os.system(temp_query)
            temp_result += 'Executing on parent shell.'
        except:
            temp_result += 'Invalid syntax or missing parameters'
    elif my_cmd[0] == 'cp':
        try:
            os.system('cp ' + my_cmd[1] + ' ' + my_cmd[2])
            temp_result += my_cmd[1] + ' copied to ' + my_cmd[2]
        except:
            temp_result += 'Invalid syntax or missing parameters'
    elif my_cmd[0] == 'ps':
        try:
            proc = subprocess.Popen(["ps"], stdout = subprocess.PIPE, shell = True)
            (out,err) = proc.communicate()
            temp_result += out
        except:
            temp_result += 'Invalid syntax or missing parameters'
    else:
        try:
            proc = subprocess.Popen(my_cmd, stdout = subprocess.PIPE, shell = True)
            (out,err) = proc.communicate()
            if out == '':
                temp_result += 'Command invalid.'
            else:
                temp_result += out
        except:
            temp_result += 'Invalid syntax or missing parameters'
    return temp_result
