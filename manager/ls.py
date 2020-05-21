import os
import yaml
import re
import __util__ as util

def ls(args):
    '''List the commands in the manager'''

    # sanity check 
    util.verify_metadata_dir()
    util.verify_internal_dir()

    # remember the current directory
    curr_dir = os.getcwd()

    # check if we only need to display the aliases
    if args.aliases:
        os.chdir(util.internal_dir())
        with open('__aliases__.sh', mode='r', encoding='utf-8') as f:
            print('Aliases defined through clmanager:')
            for i, line in enumerate(f.readlines()):
                print('{:>4}. {}'.format(str(i + 1), re.sub('^alias ', '', line.strip())))
        return

    # change to lib directory and print all file names (same as commands)
    os.chdir(util.metadata_dir())
    all_files = os.listdir()
    if not all_files:
        print('No functions or aliases have been defined yet')
    else:
        print('Registered functions:')
        for i, f in enumerate(sorted(all_files)):
            with open(f) as f:
                yaml_file = yaml.full_load(f)
                print('{:>4}. {} ({})'.format(str(i + 1), yaml_file['name'], yaml_file['command']))

    # go back to the original directory
    os.chdir(curr_dir)
