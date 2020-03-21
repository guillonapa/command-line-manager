import os
import yaml
import __util__ as util

path = os.path

def ls(args):
    '''List all the available functions and aliases in the manager'''

    # the directory where functions/aliases files live    
    util.verify_metadata_dir()

    # change to lib directory and print all file names (same as commands)
    os.chdir(util.metadata_dir())
    all_files = os.listdir()
    if not all_files:
        print('No functions or aliases have been defined yet')
    else:
        print('Loaded functions and aliases:')
        for i, f in enumerate(sorted(os.listdir())):
            with open(f) as file:
                yaml_file = yaml.full_load(file)
                print('{:>4}. {} ({})'.format(str(i + 1), yaml_file['name'], yaml_file['command']))
