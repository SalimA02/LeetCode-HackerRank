def bomberMan(n, grid):
    if n == 0 or n == 1:
        return grid
    
    r = len(grid)
    c = len(grid[0])
    
    def get_next_state(curr_grid):
        next_grid = [['O'] * c for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                if curr_grid[i][j] == 'O':
                    next_grid[i][j] = '.'
                    if i > 0: next_grid[i-1][j] = '.'
                    if i < r - 1: next_grid[i+1][j] = '.'
                    if j > 0: next_grid[i][j-1] = '.'
                    if j < c - 1: next_grid[i][j+1] = '.'
        
        return [''.join(row) for row in next_grid]
    
    if n % 2 == 0:
        return ['O' * c for _ in range(r)]
    
    grid_after_3 = get_next_state(grid)
    
    if n % 4 == 3:
        return grid_after_3
    
    grid_after_5 = get_next_state(grid_after_3)
    
    return grid_after_5
    
