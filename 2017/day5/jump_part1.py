#!/usr/bin/python

f = open('input.txt', 'r')

arr = []
for line in f.readlines():
    line = line.rstrip()
    arr.append(int(line))

#print arr
total_steps = 0
max_position = len(arr)
curr_position = 0
jump_to = 0
while curr_position < max_position:
    curr_value = arr[curr_position]

    if curr_value == 0 :
        jump_to = curr_position
    else :
        jump_to = curr_value + curr_position

    arr[curr_position] += 1
    total_steps += 1
    curr_position = jump_to

print total_steps
