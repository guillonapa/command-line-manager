import os

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

def manager_dir():
    '''Return the root directory used by clmanager'''
    return path.join(path.expanduser('~'), '.clmanager')

def lib_dir():
    '''Return the lib directory used by clmanager'''
    manager_dir = path.join(path.expanduser('~'), '.clmanager')
    return path.join(manager_dir, 'lib')