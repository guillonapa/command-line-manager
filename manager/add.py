import os
import yaml
import __util__ as util

def add(args):
    '''Add a new function or alias to the manager'''

    # sanity check
    util.verify_lib_dir()
    util.verify_metadata_dir()

    name = None
    command = None
    description = None

    if args.name:
        name = args.name
    if args.command:
        command = args.command
    if args.description:
        description = args.description

    try:
        if not name:
            name = input('Name: ')
        if not command:
            command = input('Command name: ')
        if not description:
            description = input('Description: ')
    except EOFError:
        exit(2)

    write_file({'name': name, 'command': command, 'description': description})

    create_entry_point(command)

def create_entry_point(command):
    os.chdir(util.lib_dir())
    file_name = command + '.sh'
    if not os.path.exists(file_name):
        with open(file_name, mode='w', encoding='utf-8') as f:
            print('#')
            print('# A new entry point file has been created.')
            print('# The contents of this file will be used as the body')
            print('# of a function that will be called every time you')
            print('# invoke \'' +  command + '\' from the command line.')
            print('# You may create files in the \'public\' directory and')
            print('# reference them as needed.')
            print('#')
            print('# Entry point --> ' + os.path.abspath(file_name))
            print('#')
    else:
        print('Can\'t write over file: ' + file_name)

    
def write_file(metadata):
    os.chdir(util.metadata_dir())
    ext = '.yml'

    if not os.path.exists(metadata['command'] + ext):
        file_name = metadata['command'] + ext
        with open(file=file_name, mode='w', encoding='utf-8') as f:
            yaml.dump(metadata, f)
    else:
        print('Can\'t write over file: ' + metadata['command'] + ext) 
        exit(1)