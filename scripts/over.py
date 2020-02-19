import sys
import os

def over(target=None):
    '''Get the full path of a neighboring directory (can be specified or not)
    '''
    currDir = os.path.split(os.getcwd())[-1]
    parent = os.path.split(os.getcwd())[0]
    os.chdir(parent)
    # if the directory was specified
    try:
        if target != None and target:
            os.chdir(target)
            print(os.getcwd())
            return
    except FileNotFoundError:
        sys.exit('Directory not found: ' + os.path.join(parent, target))
    # if the directory was not specified
    try:
        for dir2 in os.listdir():
            if dir2 != currDir and os.path.isdir(dir2):
                os.chdir(dir2)
                raise StopIteration(dir2)
    except StopIteration:
        print(os.getcwd())
        return
    # no other directory was found
    sys.exit('No other directories found at: ' + parent)


if __name__ == "__main__":
    over(sys.argv[1] if len(sys.argv) > 1 else None)