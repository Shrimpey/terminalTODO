#!/usr/bin/python3
import glob, os, sys

def GetLinesContaining(match, fp):
    result = []
    for num, line in enumerate(fp, 1):
        if match in line:
            result.append([line, num])
    return result

def GetStringFollowing(string, match):
    return string[string.find(match) + len(match) + 1:]

def FindTODOs(files):
    for fp in files:
        with open(fp) as file:
            for entry in GetLinesContaining(keyword, file):
                print("File\033[94m", file.name ,"\033[0mat line\033[94m", entry[1], "\033[0m")
                print("\033[93m", GetStringFollowing(entry[0], keyword), "\033[0m")

keyword = "TODO:"

os.chdir(sys.argv[1])

files = []

for arg in sys.argv[2:]:
    for file in glob.glob("*." + arg):
        files.append(file)

FindTODOs(files)
