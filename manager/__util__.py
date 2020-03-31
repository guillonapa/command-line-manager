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