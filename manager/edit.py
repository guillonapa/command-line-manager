import os
import yaml
import __util__ as util

def edit(args):
    # sanity check
    util.verify_metadata_dir()
    util.verify_lib_dir()

    for command in args.command:
        os.chdir(util.metadata_dir())
        if os.path.exists(command + '.yml'):
            print('# Editing ' + command + '.yml')

            name = None
            file_command = None
            description = None

            if args.name:
                name = args.name
            if args.command:
                file_command = args.command_name
            if args.description:
                description = args.description

            with open(command + '.yml', mode='r', encoding='utf-8') as f:
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

                    if not name.strip():
                        name = yaml_file['name']
                    if not file_command.strip():
                        file_command = yaml_file['command']
                    if not description.strip():
                        description = yaml_file['description']
                except EOFError:
                    exit(2)

            with open(command + '.yml', mode='w', encoding='utf-8') as f:
                yaml.dump({'name': name, 'command': file_command, 'description': description}, f)
            
            os.rename(command + '.yml', file_command + '.yml')
            
            os.chdir(util.lib_dir())
            os.rename(command + '.sh', file_command + '.sh')

            note = ''
            if command != file_command:
                note = ' (now ' + file_command + ')'

            print('#')
            print('# The metadata for \'' + command + '\'' + note + ' has been updated.')
            print('#')
            print('# To modify the command itself, edit:')
            print('#')
            print('#\t' + os.path.abspath(file_command + '.sh'))
