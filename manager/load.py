import os
import __util__ as util

def load(args):
    '''Genereate the '__functions.sh__' file with all declared commands.'''

    # sanity check
    util.verify_lib_dir()
    util.verify_internal_dir()

    # remember the current directory
    curr_dir = os.getcwd()

    # go to the directory with only internal resources
    os.chdir(util.internal_dir())

    # attempt to extract all contents from shell files and generate a '__functions.sh__' file
    with open('__functions__.sh', mode='w', encoding='utf-8') as func_file:
        functions = os.listdir(util.lib_dir())
        os.chdir(util.lib_dir())
        for f in functions:
            with open(f, mode='r', encoding='utf-8') as body_file:
                body = body_file.readlines()
                func_file.write('# function added for clmanager\n')
                func_file.write(util.format_function(os.path.splitext(f)[0], body))
                func_file.write('\n\n')
    
    # print a summary of the changes
    os.chdir(util.internal_dir())
    print('#')
    print('# The \'__functions__.sh\' file has been regenerated.')
    print('#')
    print('# Run the following command to load the functions:')
    print('#')
    print('# \tsource ' + os.path.abspath('__functions__.sh'))

    # go back to the original directory
    os.chdir(curr_dir)
