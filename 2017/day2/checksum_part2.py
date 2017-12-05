#!/usr/bin/python

f = open('input.txt', 'r')

total = 0
for line in f.readlines() :

    listofnums = []
    for i in line.split() :
        if i.isalnum() :
            listofnums.append(int(i))
    listofnums.sort(reverse=True)
    print(listofnums)

    index = 0
    found = False
    for num in listofnums :
        t = 0
        maxindex = len(listofnums) - 1
        while maxindex > index :
            divide = listofnums[maxindex]
            #print("%d mod %d" % (num,divide))
            if num % divide == 0 :
                t = num/divide
                found = True
                break
            maxindex -= 1

        index += 1
        if found :
            total += t
            break

print total

