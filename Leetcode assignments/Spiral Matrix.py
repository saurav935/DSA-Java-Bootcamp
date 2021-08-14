'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''

def spiralOrder(matrix):
    top = 0
    left = 0
    down = len(matrix)-1
    right = len(matrix[0])-1
    dire = 0
    arr = []

    while top <= down and left <= right:
        if dire == 0:
            for i in range(left,right+1):
                arr.append(matrix[top][i])
            top += 1

        elif dire == 1:
            for i in range(top,down+1):
                arr.append(matrix[i][right])
            right -= 1

        elif dire == 2:
            for i in range(right,left-1,-1):
                arr.append(matrix[down][i])
            down -= 1

        elif dire == 3:
            for i in range(down,top-1,-1):
                arr.append(matrix[i][left])
            left += 1

        dire = (dire+1) % 4

    return arr


