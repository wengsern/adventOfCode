#!/usr/bin/python

f = open('input.txt', 'r')

total_valid = 0
for line in f.readlines():
    listofwords = {}
    valid = True
    for i in line.split() :
        # convert string to a list and sort it
        string_list = list(i)
        string_list.sort()
        # convert list back to string
        sorted_str = ''.join(string_list)

        if not listofwords.has_key(sorted_str):
            listofwords[sorted_str] = 1
        else :
            valid = False
            break
    if valid :
        total_valid += 1

print total_valid


