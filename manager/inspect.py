import os
import __util__ as util

def inspect(args):
    # sanity check
    util.verify_lib_dir()

    os.chdir(util.lib_dir())

    for command in args.command:
        print('')
        if os.path.exists(command + '.sh'):
            print('# Contents for \'' + command + '\' (' + os.path.abspath(command + '.sh') + ')\n')
            
            lines = ''
            with open(command + '.sh', mode='r', encoding='utf-8') as f:
                for line in f.readlines():
                    lines = lines + '    ' + line

            if lines:
                print(lines)
            else:
                print('    ### The body for the command \'' + command + '\' has not been defined yet ###')
        else:
            print ('# File not found for \'' + command + '\' (' + os.path.abspath(command + '.sh') + ')')
