import os

# remember the current directory
curr_dir = os.getcwd()

# the main directory that clmanager uses
manager_dir = os.path.join(os.path.expanduser('~'), '.clmanager')
if not os.path.exists(manager_dir):
    os.chdir(os.path.expanduser('~'))
    os.mkdir('.clmanager')
    os.mkdir('.clmanager/lib')
    os.mkdir('.clmanager/internal')
    os.mkdir('.clmanager/metadata')
    os.mkdir('.clmanager/public')
else:
    os.chdir(manager_dir)
    if not os.path.exists('lib'):
        os.mkdir('lib')
    if not os.path.exists('internal'):
        os.mkdir('internal')
    if not os.path.exists('metadata'):
        os.mkdir('metadata')
    if not os.path.exists('public'):
        os.mkdir('public')
# check for the '__functions.sh__' file
os.chdir(manager_dir)
os.chdir('internal')
if not os.path.exists('__functions__.sh'):
    with open('__functions__.sh', mode='w', encoding='utf-8') as f:
        pass
    # report back
    print('#')
    print('# The \'__functions__.sh\' file has been generated.')
    print('#')
    print('# After a command has been added you will need to run:')
    print('#')
    print('# \tsource ' + os.path.abspath('__functions__.sh'))
