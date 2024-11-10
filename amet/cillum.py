def print_pyramid(n, current_row=1):
    if current_row > n:
        return
    print(' ' * (n - current_row) + '*' * (2 * current_row - 1))
    print_pyramid(n, current_row + 1)
