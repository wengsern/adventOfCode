#!/usr/bin/python

f = open('input.txt', 'r')

arr = []
for line in f.readlines():
    for x in line.split() :
        if x.isalnum() :
            arr.append(int(x))

print arr
total_cycle = 0
bank_size = len(arr)
index = 0
dict_store = {}
while True :
    # locate largest block (get index)
    index = arr.index(max(arr))
    value = arr[index]
    arr[index] = 0
    next_in = index + 1

    for i in range(value) :
        if next_in == bank_size :
            next_in = 0

        arr[next_in] = arr[next_in] + 1
        next_in += 1

    # print arr
    total_cycle += 1
    strjoin = ''.join(map(str, arr))
    if not dict_store.has_key(strjoin) :
        dict_store[strjoin] = 1
    else:
        break

print total_cycle
