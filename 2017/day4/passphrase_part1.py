#!/usr/bin/python

f = open('input.txt', 'r')

total_valid = 0

for line in f.readlines():
    listofwords = {}
    valid = True
    for i in line.split() :
        if not listofwords.has_key(i):
            listofwords[i] = 1
        else :
            valid = False
            break
    if valid :
        total_valid += 1

print total_valid
