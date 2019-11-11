def find_lcs(a, b):
    row_len = len(b)
    col_len = len(a)
    grid = [[0] * col_len for i in range(row_len)]
    largest = 0
    for i in range(row_len):
        for j in range(col_len):
            if a[j] == b[i]:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = 0
            largest = max(largest, grid[i][j])
    return largest


print(find_lcs("blue", "clues"))
