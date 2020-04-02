import os
import argparse
from add import add
from rm import rm
from ls import ls
from edit import edit
from inspect import inspect
from load import load

path = os.path

def verify_clmanager_dir():
    '''Verify that the root directory used by clmanager exists'''

    # the main directory that clmanager uses
    manager_dir = path.join(path.expanduser('~'), '.clmanager')
    if not path.exists(manager_dir):
        print('Command line manager directory does not exists: \n\t{}'.format(manager_dir))
        exit(1)

def verify_lib_dir():
    '''Verify that the \'lib\' directory used by clmanager exists'''

    verify_clmanager_dir()

    # we can safely assume that the manager directory exists now
    manager_dir = path.join(path.expanduser('~'), '.clmanager')

    # the directory where functions/aliases files live    
    lib_dir = path.join(manager_dir, 'lib')
    if not path.exists(lib_dir):
        print('The \'lib\' directory does not exist: \n\t{}'.format(lib_dir))
        exit(1)

def verify_internal_dir():
    '''Verify that the \'internal\' directory used by clmanager exists'''

    verify_clmanager_dir()

    # we can safely assume that the manager directory exists now
    manager_dir = path.join(path.expanduser('~'), '.clmanager')

    # the directory where functions/aliases files live    
    internal_dir = path.join(manager_dir, 'internal')
    if not path.exists(internal_dir):
        print('The \'lib\' directory does not exist: \n\t{}'.format(internal_dir))
        exit(1)

def verify_metadata_dir():
    '''Verify that the \'metadata\' directory used by clmanager exists'''

    verify_clmanager_dir()

    # we can safely assume that the manager directory exists now
    manager_dir = path.join(path.expanduser('~'), '.clmanager')

    # the directory where functions/aliases files live    
    metadata_dir = path.join(manager_dir, 'metadata')
    if not path.exists(metadata_dir):
        print('The \'metadata\' directory does not exist: \n\t{}'.format(metadata_dir))
        exit(1)

def manager_dir():
    '''Return the root directory used by clmanager'''
    return path.join(path.expanduser('~'), '.clmanager')

def lib_dir():
    '''Return the lib directory used by clmanager'''
    manager_dir = path.join(path.expanduser('~'), '.clmanager')
    return path.join(manager_dir, 'lib')

def internal_dir():
    '''Return the internal directory used by clmanager'''
    manager_dir = path.join(path.expanduser('~'), '.clmanager')
    return path.join(manager_dir, 'internal')

def metadata_dir():
    '''Return the metadata directory used by clmanager'''
    manager_dir = path.join(path.expanduser('~'), '.clmanager')
    return path.join(manager_dir, 'metadata')

def format_function(name, body):
    '''Return a string with the generated function using the name and the body passed as arguments'''
    body_string = '\t'.join(body)
    if not body_string:
        function_file = os.path.abspath(os.path.join(lib_dir(), name + '.sh'))
        body_string = 'echo "# The body for the command \'' + name + '\' has not been defined yet."'
        body_string = body_string + '\n\techo "#"' + '\n\techo "# Enter your code in:"' + '\n\techo "#"' + '\n\techo "#\t' + function_file + '"'

    return 'function {}() {{\n\t{}\n}}'.format(name, body_string)

def metadata_file_name(command):
    '''Return the name of the metadata file for the command'''
    return str(command) + '.yml'

def shell_file_name(command):
    '''Return the name of the shell file for the command'''
    return str(command) + '.sh'

def help(args):
    '''Additional help for the manager.'''
    print('\n\tAdditional help for the manager\n'
            '\n\tO       o O       o O       o'
            '\n\t| O   o | | O   o | | O   o |'
            '\n\t| | O | | | | O | | | | O | |'
            '\n\t| o   O | | o   O | | o   O |'
            '\n\to       O o       O o       O')

def repl_it(argv):
    # the main argument parser
    parser = argparse.ArgumentParser(description='Command line manager for user defined commands.')

    # subparsers for subcommands
    subparsers = parser.add_subparsers(help='sub-command help')
    parser_add = subparsers.add_parser('add', help='Add a new command')
    parser_rm = subparsers.add_parser('rm', help='Remove a command')
    parser_ls = subparsers.add_parser('ls', help='List all commands')
    parser_edit = subparsers.add_parser('edit', help='Edit a command')
    parser_inspect = subparsers.add_parser('inspect', help='Inspect the body of a command')
    parser_load = subparsers.add_parser('load', help='Generate the \'__functions.sh__\' file with all commands')
    parser_help = subparsers.add_parser('help', help='Display additional help for the manager')

    # add the default functions for the subcommands
    parser_add.set_defaults(func=add)
    parser_rm.set_defaults(func=rm)
    parser_ls.set_defaults(func=ls)
    parser_edit.set_defaults(func=edit)
    parser_inspect.set_defaults(func=inspect)
    parser_load.set_defaults(func=load)
    parser_help.set_defaults(func=help)

    # add additional arguments to the 'inspect' subcommand
    parser_inspect.add_argument('command', help='The command to be inspected', nargs='+')

    # add additional arguments to the 'rm' subcommand
    parser_rm.add_argument('command', help='The command to be deleted from the registry', nargs='+')

    # add additional arguments to the 'edit' subcommand
    parser_edit.add_argument('command', help='The command to be edited', nargs=1)
    parser_edit.add_argument('-c', '--command-name', help='The name that will be used to register the command', type=str)
    parser_edit.add_argument('-n', '--name', help='A human-readable name to identify the command', type=str)
    parser_edit.add_argument('-d', '--description', help='A brief description of what the command does', type=str)

    # add additional arguments to the 'add' subcommand
    parser_add.add_argument('-c', '--command', help='The name that will be used to register the comand', type=str)
    parser_add.add_argument('-n', '--name', help='A human-readable name to identify the command', type=str)
    parser_add.add_argument('-d', '--description', help='A brief description of what the command does', type=str)

    # add additional arguments to the 'load' subcommand
    parser_load.add_argument('-q', '--quiet', help='Do not print anything to stdout', action='store_const', const=True)

    # add the default function for the main parser
    parser.set_defaults(func=help)

    # parse the arguments
    args = parser.parse_args(argv)

    # apply the appropriate default function
    args.func(args)
