import os
import yaml
import __util__ as util

def edit(args):
    '''Edit an existing command in the manager'''

    # sanity check
    util.verify_metadata_dir()
    util.verify_lib_dir()

    # remember the current directory
    curr_dir = os.getcwd()

    # at the moment args.command should always be an array of one element
    for command in args.command:
        # make sure we are on the right directory
        os.chdir(util.metadata_dir())
        # the name of the metadata file
        metadata_file_name = util.metadata_file_name(command)
        # verify that the file actually exists
        if os.path.exists(metadata_file_name):
            print('# Editing ' + metadata_file_name)
            # the metadata needed
            name = None
            file_command = None
            description = None
            # extract any info available in flags
            if args.name:
                name = args.name
            if args.command:
                file_command = args.command_name
            if args.description:
                description = args.description
            # open the file to update to read existing contents and prompt for new values
            with open(metadata_file_name, mode='r', encoding='utf-8') as f:
                yaml_file = yaml.full_load(f)
                try:
                    if not name:
                        name = input('Name (' + yaml_file['name'] + '): ')
                    if not file_command:
                        file_command = input('Command name (' + yaml_file['command'] + '): ')
                    if not description:
                        description_postfix = ''
                        if len(yaml_file['description']) > 10:
                            description_postfix = '...'
                        description = input('Description (' + yaml_file['description'][:10] + description_postfix + '): ')
                    # only save values that are not empty strings
                    if not name.strip():
                        name = yaml_file['name']
                    if not file_command.strip():
                        file_command = yaml_file['command']
                    if not description.strip():
                        description = yaml_file['description']
                except EOFError:
                    exit(2)

            # attempt to rewrite the metadata file
            with open(metadata_file_name, mode='w', encoding='utf-8') as f:
                yaml.dump({'name': name, 'command': file_command, 'description': description}, f)
            
            # rename the file to match the new command name
            os.rename(metadata_file_name, util.metadata_file_name(file_command))
            
            # go to the directory with all shell files
            os.chdir(util.lib_dir())
            # rename the corresponding shell file to match the new command name
            os.rename(util.shell_file_name(command), util.shell_file_name(file_command))

            # print a summary message of the changes
            note = ''
            if command != file_command:
                note = ' (now ' + file_command + ')'
            print('#')
            print('# The metadata for \'' + command + '\'' + note + ' has been updated.')
            print('#')
            print('# To modify the command itself, edit:')
            print('#')
            print('#\t' + os.path.abspath(file_command + '.sh'))
    
    # return to the original directory
    os.chdir(curr_dir)
