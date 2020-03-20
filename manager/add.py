import os
import __util__ as util

def add(args):
    '''Add a new function or alias to the manager'''

    # sanity check
    util.verify_lib_dir()

    if args.name:
        print('Name: ' + args.name)
    if args.command:
        print('Command: ' + args.command)
    if args.description:
        print('Description: ' + args.description)
