def hourglassSum(arr):
    rows = len(arr)
    sum_hour_glass = -9999999
    for row in range(rows-2):
        step_column = 0
        while step_column < 5:
            head_row = arr[row][step_column:step_column+3]
            mid_row = arr[row+1][step_column + 1]
            back_row = arr[row+2][step_column:step_column+3]
            sum_of_row = sum(head_row) + mid_row + sum(back_row)
            sum_hour_glass = max(sum_of_row, sum_hour_glass)
            step_column = step_column + 1
    return sum_hour_glass

if __name__ == "__main__":
    arr = [
        [1,1,1,0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1 ,1 ,1 ,0 ,0 ,0],
       [0 ,0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0,0, 1, 2, 4, 0],
    ]
    result = hourglassSum(arr)
    print(result)