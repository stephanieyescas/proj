#!/usr/bin/env python3

"""
Stanford CS106A BabyNames Project
Part-A : organizing the bulk data
"""

import sys


def add_name(names, year, rank, name):
    """
    Add the given data: int year, int rank, str name
    to the given names dict and return it.
    (1 test provided, more tests TBD)
    >>> add_name({}, 2000, 10, 'abe')
    {'abe': {2000: 10}}
    >>> add_name({}, 1990, 30, 'john')
    {'john': {1990: 30}}
    """
    if name not in names:
        names[name] = {year:rank}
    if name in names:
        inner = names[name]
        if year in inner:
            if inner[year] < rank:
                return names
        inner[year] = rank
    return names







def add_file(names, filename):
    """
    Given a names dict and babydata.txt filename, add the file's data
    to the dict and return it.
    (Tests provided, Code TBD)
    >>> add_file({}, 'small-2000.txt')
    {'A': {2000: 1}, 'B': {2000: 1}, 'C': {2000: 2}}
    >>> add_file({}, 'small-2010.txt')
    {'C': {2010: 1}, 'D': {2010: 1}, 'A': {2010: 2}, 'E': {2010: 2}}
    >>> add_file({'A': {2000: 1}, 'B': {2000: 1}, 'C': {2000: 2}}, 'small-2010.txt')
    {'A': {2000: 1, 2010: 2}, 'B': {2000: 1}, 'C': {2000: 2, 2010: 1}, 'D': {2010: 1}, 'E': {2010: 2}}
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        year = int(lines[0])
        lines.pop(0)
        for line in lines:
            remove = line.replace(' ','')
            remove = remove.replace('\n', '')
            list = remove.split(',')
            rank = int(list[0])
            firstname = list[1]
            secondname = list[2]
            add_name(names, year, rank, firstname)
            add_name(names, year, rank, secondname)
        return names


def read_files(filenames):
    """
    Given list of filenames, build and return a names dict
    of all their data.
    """
    names_dict = {}
    for filename in filenames:
        add_file(names_dict, filename)
    return names_dict




def search_names(names, target):
    """
    Given names dict and a target string,
    return a sorted list of all the name strings
    that contain that target string anywhere.
    Not case sensitive.
    (Code and tests TBD)
    >>> search_names({'Aaliyah': {2010: 1}}, 'aa')
    ['Aaliyah']
    >>> search_names({'Aaron': {2010: 1}}, 'aa')
    ['Aaron']
    >>> search_names({'Bbenett': {2010: 1}}, 'Bb')
    ['Bbenett']
    """
    lst = []
    target = target.lower()
    for name in names.keys():
        namelower = name.lower()
        if target in namelower:
            lst.append(name)
    return sorted(lst)


def print_names(names):
    """
    (provided)
    Given names dict, print out all its data, one name per line.
    The names are printed in increasing alphabetical order,
    with its years data also in increasing order, like:
    Aaden [(2010, 560)]
    Aaliyah [(2000, 211), (2010, 56)]
    ...
    Surprisingly, this can be done with 2 lines of code.
    We'll explore this in lecture.
    """
    for key, value in sorted(names.items()):
        print(key, sorted(value.items()))


def main():
    # (provided)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Change filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
