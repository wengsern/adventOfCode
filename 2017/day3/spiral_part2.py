#!/usr/bin/python

input_int=347991

north=(0,1)
north_east=(1,1)
north_west=(-1,1)
south=(0,-1)
south_east=(1,-1)
south_west=(-1,-1)
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

def get_sum_value(matrix, cur_coor) :
    check_n = matrix.has_key(sum_coordinates(cur_coor, north))
    check_ne = matrix.has_key(sum_coordinates(cur_coor, north_east))
    check_nw = matrix.has_key(sum_coordinates(cur_coor, north_west))
    check_s = matrix.has_key(sum_coordinates(cur_coor, south))
    check_se = matrix.has_key(sum_coordinates(cur_coor, south_east))
    check_sw = matrix.has_key(sum_coordinates(cur_coor, south_west))
    check_e = matrix.has_key(sum_coordinates(cur_coor, east))
    check_w = matrix.has_key(sum_coordinates(cur_coor, west))

    checksum = 0
    if check_n :
        checksum += matrix[sum_coordinates(cur_coor, north)]
    if check_ne :
        checksum += matrix[sum_coordinates(cur_coor, north_east)]
    if check_nw :
        checksum += matrix[sum_coordinates(cur_coor, north_west)]
    if check_s :
        checksum += matrix[sum_coordinates(cur_coor, south)]
    if check_se :
        checksum += matrix[sum_coordinates(cur_coor, south_east)]
    if check_sw :
        checksum += matrix[sum_coordinates(cur_coor, south_west)]
    if check_e :
        checksum += matrix[sum_coordinates(cur_coor, east)]
    if check_w :
        checksum += matrix[sum_coordinates(cur_coor, west)]

    return checksum

# sum two coordinates
def sum_coordinates(c1, c2):
    return tuple(map(lambda x, y: x + y, c1, c2))

# dict = [ (0,0):1 , (1,0):2, (1,1):3, (  ]
matrix={}
coordinate = (0,0)
prev = (0,0)
for i in range(input_int):
    value = i + 1

    if value == 1 :
        checksum = 1
    elif value == 2 :
        coordinate = (1,0)
        checksum = 1
    else:
        direction = check_next_move(matrix, coordinate)
        coordinate = sum_coordinates(prev, direction)

    matrix[coordinate] = checksum
    if value > 2 :
        checksum = get_sum_value(matrix, coordinate)
        matrix[coordinate] = checksum

    prev = coordinate
    # break condition as we found the next larger
    if checksum > input_int :
        break

#print matrix
print coordinate
print matrix[coordinate]
