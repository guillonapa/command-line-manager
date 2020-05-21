import os
import yaml
import __util__ as util


def add(args):
    '''Add a new command to the manager'''

    # sanity check
    util.verify_lib_dir()
    util.verify_metadata_dir()

    name = None
    command = None
    description = None

    if args.alias:
        add_alias(args.alias)
        return

    # get the values of any flags that were passed
    if args.name:
        name = args.name
    if args.command:
        command = args.command
    if args.description:
        description = args.description

    # get the remaining data from stdin if not all flags were passed
    try:
        if not name:
            name = input('Name: ')
        if not command:
            command = input('Command name: ')
        if not description:
            description = input('Description: ')
    except EOFError:
        exit(2)

    # write the metadata file
    write_file({'name': name, 'command': command, 'description': description})

    # create the shell file in lib
    create_entry_point(command)


def add_alias(alias):
    '''Add an alias to the manager'''
    
    # remember the current directory
    curr_dir = os.getcwd()

    # add the alias to the __aliases__.sh file
    os.chdir(util.internal_dir())
    with open('__aliases__.sh', mode='a', encoding='utf-8') as f:
        f.write(util.format_alias(alias))

    # return to the current directory
    os.chdir(curr_dir)


def create_entry_point(command):
    '''Create an empty shell file in the 'lib' directory for the command's body'''
    
    # remember the current directory
    curr_dir = os.getcwd()
    # go to the root directory where shell files exist for the manager
    os.chdir(util.lib_dir())
    # attempt to write the file
    file_name = util.shell_file_name(command)
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
        exit(1)
    # return to the current directory
    os.chdir(curr_dir)

    
def write_file(metadata):
    '''Generate the metadata file for the new command in the 'metadata' directory'''

    # remember the current directory
    curr_dir = os.getcwd()
    # go to the root directory where all metadata files exist for the manager
    os.chdir(util.metadata_dir())
    # attempt to write the file
    file_name = util.metadata_file_name(metadata['command'])
    if not os.path.exists(file_name):
        with open(file=file_name, mode='w', encoding='utf-8') as f:
            yaml.dump(metadata, f)
    else:
        print('Can\'t write over file: ' + file_name) 
        exit(1)
    # return to the current directory
    os.chdir(curr_dir)
