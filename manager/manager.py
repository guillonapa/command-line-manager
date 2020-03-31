import argparse
from add import add
from rm import rm
from ls import ls
from edit import edit
from inspect import inspect
from load import load

def help(args):
    '''Additional help for the manager.'''
    print('\n\tAdditional help for the manager\n'
            '\n\tO       o O       o O       o'
            '\n\t| O   o | | O   o | | O   o |'
            '\n\t| | O | | | | O | | | | O | |'
            '\n\t| o   O | | o   O | | o   O |'
            '\n\to       O o       O o       O')

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

# add the default function for the main parser
parser.set_defaults(func=help)

# parse the arguments
args = parser.parse_args()

# apply the appropriate default function
args.func(args)
