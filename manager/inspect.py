import os
import __util__ as util

def inspect(args):
    '''Print the body of the command'''

    # sanity check
    util.verify_lib_dir()

    # remember the current directory
    curr_dir = os.getcwd()

    # go to the directory containing all shell files
    os.chdir(util.lib_dir())

    # try to print the body of each command
    for command in args.command:
        print('')
        if os.path.exists(command + '.sh'):
            print('# Contents for \'' + command + '\' (' + os.path.abspath(command + '.sh') + ')\n')
            # the actual contents of the shell file
            lines = ''
            with open(command + '.sh', mode='r', encoding='utf-8') as f:
                for line in f.readlines():
                    lines = lines + '    ' + line
            # show a message if the file is empty
            if lines:
                print(lines)
            else:
                print('    ### The body for the command \'' + command + '\' has not been defined yet ###')
        else:
            print ('# File not found for \'' + command + '\' (' + os.path.abspath(command + '.sh') + ')')
    
    # go back to the original directory
    os.chdir(curr_dir)
