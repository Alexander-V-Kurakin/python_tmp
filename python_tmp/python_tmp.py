#!/usr/bin/python3

import sys

print ('Hello, Python!')

print ('Number of arguments:', len(sys.argv), 'arguments')
print ('Arguments list:', str(sys.argv))

str = input('\nInput a string and press enter to exit ')
print (str)


# The output is
#
# ./python_tmp.py
#
# Hello, Python!
# Number of arguments: 1 arguments
# Arguments list: ['./python_tmp.py']
#
# Input a string and press enter to exit <string wasn't entered'>
#
# where sys.argv[0] is the program i. e. script name


# The program could be run with arguments list
#
# ./python_tmp.py arg1 arg2 arg3
#
# Then the output is
#
# Hello, Python!
# Number of arguments: 4 arguments
# Arguments list: ['./python_tmp.py', 'arg1', 'arg2', 'arg3']
#
# Input a string and press enter to exit str1 str2 str3 str_n
# str1 str2 str3 str_n
