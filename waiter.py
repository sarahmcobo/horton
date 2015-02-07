# This program will check for the existence of a file named ..._waiter.txt in the top level
# of ePubChef (the level of cook.py). It runs from the level, but will look accross parallel
# ePubChef folders as well.
#
# If ...._waiter.txt is found, it will trigger a run of cook.py in that directory, then delete
# ..._waiter.txt.

# first just look in current dir
import os
from os.path import isfile, join
import subprocess

cook_dir = os.path.dirname(os.path.realpath(__file__))
print("cook_dir", cook_dir)

def list_dirs():
    return [cook_dir] # for now

def get_waiters_attention():
    #open and read first line arguments
    try:
        with open(recipe_loc, 'r') as f:
            _recipe = yaml.load(f)
    except:
        print('\n***Error in waiter.txt file*** :')
        raise SystemExit
    f.close()

def find_and_run(a_directory):
    # test for presents of waiter.txt
    if os.path.exists(join(a_directory, 'waiter.txt')):
        print("waiter.txt exists")
        args = read_args(a_directory)
        output = subprocess.check_output(['python','cook.py',args[0], '>','cook.log'], shell=True)
    else:
        print("waiter is ignoring you")

def read_args(a_directory):
    f = open(join(a_directory, 'waiter.txt'), 'r')
    args = f.readlines()[0].strip().split(" ")
    print("args:", args)
    f.close()

    return(args)
######################################
# main processing
dirs = list_dirs()
for directory in dirs:
    find_and_run(directory)
    print("See cook.log in: ", dirs)
