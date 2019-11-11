attractions = {
    "WEST MINISTER ABBY": (0.5, 7),
    "GLOBE THEATER": (0.5, 6),
    "NATIONAL GALLERY": (1, 9),
    "BRITISH MUSEUM": (2, 9),
    "ST.PAUL'S CATHEDRAL": (0.5, 8)
}


def hash_to_index(a, b):
    return round((a / b) - 1)


def index_to_hash(a, b):
    return (a + 1) * b


def calculate_travel_itinerary(attractions: dict):
    attr = [i for i in attractions.keys()]
    days = [attractions[i][0] for i in attractions.keys()]
    rates = [attractions[i][1] for i in attractions.keys()]
    row_len = len(attractions)  # find rows from size of hash map
    col_max = max(days)  # find max range from days
    col_min = min(days)  # find min range from days
    col_len = round((col_max / col_min))  # calculate column length from max and min
    grid = [[(0, [])] * col_len for i in range(row_len)]  # initialize grid with zeros
    for i in range(row_len):
        for j in range(col_len):
            previous_max, _ = grid[i - 1][j]
            days_diff = index_to_hash(j, col_min) - days[i]  # current column days - current destination days
            remaining_space_idx = hash_to_index(days_diff, col_min)  # remaining space estimate
            current = 0
            if days_diff >= 0:
                current = rates[i]
            remaining_space = 0
            if remaining_space_idx >= 0:
                remaining_space, _ = grid[i - 1][remaining_space_idx]
            proposed = current + remaining_space
            if proposed > previous_max:
                grid[i][j] = (proposed, grid[i - 1][remaining_space_idx][1].copy())
                grid[i][j][1].append(attr[i])
            else:
                grid[i][j] = (previous_max, grid[i - 1][j][1].copy())
    return grid[row_len - 1][col_len - 1]


def calculate_items():
    items = {
        "Water": (3, 10),
        "Book": (1, 3),
        "Food": (2, 9),
        "Jacket": (2, 5),
        "Camera": (1, 6)
    }
    rows_len = 5
    col_len = 6
    names = [i for i in items.keys()]
    values = [items[i] for i in items.keys()]
    grid = [[(0, [])] * col_len for i in range(rows_len)]
    for i in range(rows_len):
        for j in range(col_len):
            previous_rk, previous_it = grid[i - 1][j]
            curr_wt, curr_rk = values[i]
            weight_diff = (j + 1) - curr_wt
            rem_idx = weight_diff - 1
            rem_rk, rem_it = grid[i - 1][rem_idx]
            if weight_diff < 0:
                curr_rk = 0
            if rem_idx < 0:
                rem_rk = 0
                rem_it = []
            proposed = curr_rk + rem_rk
            if proposed > previous_rk:
                new_it = rem_it.copy()
                new_it.append(names[i])
                grid[i][j] = (proposed, new_it)
            else:
                grid[i][j] = (previous_rk, previous_it.copy())
    return grid[rows_len - 1][col_len - 1]


