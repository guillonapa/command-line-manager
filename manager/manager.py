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
parser = argparse.ArgumentParser(description='Command line manager for user defined functions and aliases.')

# subparsers for subcommands
subparsers = parser.add_subparsers(help='sub-command help')
parser_add = subparsers.add_parser('add', help='Add a new function or alias')
parser_rm = subparsers.add_parser('rm', help='Remove a function or alias')
parser_ls = subparsers.add_parser('ls', help='List all functions or aliases')
parser_edit = subparsers.add_parser('edit', help='Edit a function or alias')
parser_inspect = subparsers.add_parser('inspect', help='Inspect the code for a function or alias')
parser_load = subparsers.add_parser('load', help='Load all the available functions and aliases')
parser_help = subparsers.add_parser('help', help='Display additional help for the manager')

# add the default functions for the subcommands
parser_add.set_defaults(func=add)
parser_rm.set_defaults(func=rm)
parser_ls.set_defaults(func=ls)
parser_edit.set_defaults(func=edit)
parser_inspect.set_defaults(func=inspect)
parser_load.set_defaults(func=load)
parser_help.set_defaults(func=help)

parser_inspect.add_argument('command', help='The command to be inspected', nargs='+')

# add additional arguments to the 'add' subcommand
parser_add.add_argument('-c', '--command', help='The name that will be used to register the function', type=str)
parser_add.add_argument('-n', '--name', help='A human-readable name to identify the function', type=str)
parser_add.add_argument('-d', '--description', help='A brief description of what the function does', type=str)

# add the default function for the main parser
parser.set_defaults(func=help)

# parse the arguments
args = parser.parse_args()

# apply the appropriate default function
args.func(args)
