# !/usr/bin/python

import sys

print 'Hello, Python!'

print 'Number of arguments:', len(sys.argv), 'arguments'
print 'Arguments list:', str(sys.argv)


# The output is
#
# Hello, Python!
# Number of arguments: 1 arguments
# Arguments list: ['python_tmp.py']
#
# where sys.argv[0] is the program i. e. script name


# The program could be run with arguments list
#
# ./python_tmp.py arg1 arg2 arg3

# Then the output is
#
# Hello, Python!
# Number of arguments: 4 arguments
# Arguments list: ['./python_tmp.py', 'arg1', 'arg2', 'arg3']
