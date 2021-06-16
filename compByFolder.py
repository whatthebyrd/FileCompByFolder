#!/usr/bin/env python3

# compByFolder
# Invoke by: compByFolder <FolderPath1> <FolderPath2>
# Takes all files in 2 designated folders and compares matching filenames' contents
# Original Creation: 09NOV20
# Released under Apache 2.0 License

import os  # For checking file path and replacing file extension
import sys  # For parsing input arguments
import filecmp  # For comparing files

if os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2]):  # Check if dir paths are valid
    files1 = {f for f in os.listdir(sys.argv[1]) if os.path.isfile(os.path.join(sys.argv[1], f))}  # List files in dir 1
    files2 = {f for f in os.listdir(sys.argv[2]) if os.path.isfile(os.path.join(sys.argv[2], f))}  # List files in dir 2
    files1A = sorted(files1)  # Alphabetize files in dir 1
    files2A = sorted(files2)  # Alphabetize files in dir 2
    fileCt = 0

    if files1A == files2A:  # Check if both directories match
        for i in range(len(files1A)):  # Begin comparing files
            if not filecmp.cmp(os.path.join(sys.argv[1], files1A[i]), os.path.join(sys.argv[2], files2A[i])):
                print("File: " + files1A[i] + " has changes.")
            fileCt += 1
        print(str(fileCt) + " files checked.")
    else:  # If both dirs do NOT match, list diffs and then compare:
        both = sorted(files1 & files2)  # List files present in both folders and sort files alphabetically
        notBoth = sorted(files1 ^ files2)  # List files NOT present in both folders and sort files alphabetically
        print(str(len(notBoth)) + " file(s) not in both:\n" + str(notBoth))
        for i in range(len(both)):  # Begin comparing files
            if not filecmp.cmp(os.path.join(sys.argv[1], both[i]), os.path.join(sys.argv[2], both[i])):
                print("File: " + both[i] + " has changes.")
            fileCt += 1
        print(str(fileCt) + " files checked.")

else:
    print("Error: Folder paths invalid. Exiting.")
