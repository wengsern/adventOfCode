#!/usr/bin/python

f = open('input.txt', 'r')

string = f.read()
l=[]
for char in string.rstrip():
    l.append(char)

total = 0;
for index in range(len(l)):
    j = index + 1
    if index==len(l)-1:
        j = 0

    print("index=%s j=%s\n" % (index,j))

    if int(l[index]) == int(l[j]):
        total = total + int(l[index])

    print(l[index], l[j])

print total
