def find_lcs(a, b):
    col_len = len(a)
    row_len = len(b)
    grid = [[0] * col_len for i in range(row_len)]
    largest = 0
    for i in range(row_len):
        for j in range(col_len):
            if a[j] == b[i]:
                grid[i][j] = grid[i - 1][j - 1] + 1  # top lef
            else:
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])
            largest = max(largest, grid[i][j])
    return largest


print(find_lcs("fosh", "fish"))
