import os
import __util__ as util
import load

def rm(args):
    '''Remove a command from the manager'''

    #sanity check
    util.verify_lib_dir()
    util.verify_metadata_dir()

    # remember the current directory
    curr_dir = os.getcwd()

    # iterate through the commands to remove
    for command in args.command:
        # first from metadata
        metadata_file_name = util.metadata_file_name(command)
        os.chdir(util.metadata_dir())
        if os.path.exists(metadata_file_name):
            os.remove(metadata_file_name)
        else:
            print('File not found: ' + metadata_file_name)
        # then from lib
        shell_file_name = util.shell_file_name(command)
        os.chdir(util.lib_dir())
        if os.path.exists(shell_file_name):
            os.remove(shell_file_name)
        else:
            print('File not found: ' + shell_file_name)

    # regenerate the __functions__.sh file
    load.load(args)