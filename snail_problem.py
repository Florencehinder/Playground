def snail(array):
    #Starting position
    y = 0
    x = 0
    direction = 'Right'
    lst = [0]*len(array)*len(array[0])
    visited = array

    def change_direction(direction):
        #function that inputs the previous direction and outputs the new direction
        if direction == 'Right':
            return 'Down'
        elif direction == 'Down':
            return 'Left'
        elif direction == 'Left':
            return 'Up'
        elif direction == 'Up':
            return 'Right'

    def position_update(direction, y, x):
        #Function that inputs direction and previous y, x locations, to output new y, x locations
        if direction == 'Right':
            x = x + 1
        elif direction == 'Down':
            y = y + 1
        elif direction == 'Left':
            x = x - 1
        elif direction == 'Up':
            y = y - 1
        return y, x

    #Check length of array to make sure processing is necessary
    if len(array) <=1:
        lst = array[0]
    else:
        #If snail reaches the end of the array, change direction
        array_len = len(array)*len(array[0])
        for i in range(array_len): #0 to 8
            if x == len(array)-1 and y ==0 or y==len(array)-1 and x ==len(array)-1 or y==len(array)-1 and x == 0 :
                direction = change_direction(direction)
            elif visited[position_update(direction, y, x)[0]][position_update(direction, y, x)[1]] == '*':
                #change direction if you reach the boundary or are in a cell already visited
                direction = change_direction(direction)

            lst[i] = array[y][x]
            visited[y][x] = '*'
            # update position
            (y, x) = position_update(direction, y, x)

    return lst