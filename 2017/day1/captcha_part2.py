#!/usr/bin/python

f = open('input.txt', 'r')

string = f.read()
l=[]
for char in string.rstrip():
    l.append(char)

total = 0;
half = len(l)/2
length = len(l)
for index in range(length):
    jump = (index + half)%length

    print("index=%s j=%s" % (index,jump))

    if int(l[index]) == int(l[jump]):
        total = total + int(l[index])

   print(l[index], l[jump])

print total
