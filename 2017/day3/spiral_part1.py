#!/usr/bin/python

input_int=347991

north=(0,1)
south=(0,-1)
east=(1,0)
west=(-1,0)
def check_next_move(matrix, cur_coor) :
    check_n = matrix.has_key(sum_coordinates(cur_coor, north))
    check_s = matrix.has_key(sum_coordinates(cur_coor, south))
    check_e = matrix.has_key(sum_coordinates(cur_coor, east))
    check_w = matrix.has_key(sum_coordinates(cur_coor, west))

    if(check_n == False and check_s == False and check_e == False and check_w == True):
        direction = north
    elif(check_n == False and check_s == True and check_e == False and check_w == True):
        direction = north
    elif(check_n == False and check_s == True and check_e == False and check_w == False):
        direction = west
    elif(check_n == False and check_s == True and check_e == True and check_w == False):
        direction = west
    elif(check_n == False and check_s == False and check_e == True and check_w == False):
        direction = south
    elif(check_n == True and check_s == False and check_e == True and check_w == False):
        direction = south
    elif(check_n == True and check_s == False and check_e == False and check_w == False):
        direction = east
    elif(check_n == True and check_s == False and check_e == False and check_w == True):
        direction = east

    return direction


# sum two coordinates
def sum_coordinates(c1, c2):
    return tuple(map(lambda x, y: x + y, c1, c2))

# dict = [ (0,0):1 , (1,0):2, (1,1):3, (  ]
matrix={}
prev = (0,0)
for i in range(input_int):
    value = i + 1

    if value == 1 :
        coordinate = (0,0)
    elif value == 2 :
        coordinate = (1,0)
    else:
        direction=check_next_move(matrix, coordinate)
        coordinate = sum_coordinates(prev, direction)

    matrix[coordinate] = value
    prev = coordinate

#print matrix
print prev

x, y = prev
distance = abs(x) +abs(y)
print distance
