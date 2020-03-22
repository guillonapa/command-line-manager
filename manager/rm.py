import os
import __util__ as util
import load

def rm(args):
    #sanity check
    util.verify_lib_dir()
    util.verify_metadata_dir()

    for command in args.command:
        # first from metadata
        os.chdir(util.metadata_dir())
        if os.path.exists(command + '.yml'):
            os.remove(command + '.yml')
        else:
            print('File not found: ' + command + '.yml')

        # then from lib
        os.chdir(util.lib_dir())
        if os.path.exists(command + '.sh'):
            os.remove(command + '.sh')
        else:
            print('File not found: ' + command + '.sh')

    # regenerate the __functions__.sh file
    load.load(args)