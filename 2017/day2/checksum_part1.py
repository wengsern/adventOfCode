#!/usr/bin/python

f = open('input.txt', 'r')

total = 0
for line in f.readlines() :

    listofnums = []
    for i in line.split() :
        if i.isalnum() :
            listofnums.append(int(i))
    listofnums.sort()
    #print(listofnums)

    total = total + (listofnums[-1] - listofnums[0])

print total

