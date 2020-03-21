import os
import __util__ as util

def load(args):
    # sanity check
    util.verify_lib_dir()
    util.verify_internal_dir()

    os.chdir(util.internal_dir())

    with open('__functions__.sh', mode='w', encoding='utf-8') as func_file:
        functions = os.listdir(util.lib_dir())
        os.chdir(util.lib_dir())
        for f in functions:
            with open(f, mode='r', encoding='utf-8') as body_file:
                body = body_file.readlines()
                func_file.write('# function added for clmanager\n')
                func_file.write(util.format_function(os.path.splitext(f)[0], body))
                func_file.write('\n\n')
    
    os.chdir(util.internal_dir())
    # os.system('source ' + '__functions__.sh')

    print('#')
    print('# Run the following command to load the functions:')
    print('#')
    print('# \tsource ' + os.path.abspath('__functions__.sh'))
