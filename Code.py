import sys

# Creating the n x m Grid
class Grid:
    def __init__(self, n, m):
        # Initializing the grid
        self.rows = n
        self.cols = m
        self.grid = [[0] * m for _ in range(n)]

    def set_obstacle(self, row, col):
        # Logic to mark a cell as an obstacle
        self.grid[row][col] = -1

    def set_start_point(self, row, col):
        # Logic for setting up the start point in the grid
        self.start = (row, col)

    def set_end_point(self, row, col):
        # Logic for setting up the end point in the grid
        self.end = (row, col)


# Method to find the optimal path and cost
def find_optimal_path(grid):
    start = grid.start
    end = grid.end

    rows, cols = grid.rows, grid.cols
    # Initializing a 2D table to store minimum costs
    dp = [[float('inf')] * cols for _ in range(rows)]
    dp[start[0]][start[1]] = 0
    
    # Logic to fill in the dp table using dyanimc programming
    for r in range(rows):
        for c in range(cols):
            # Skipping obstacles
            if grid.grid[r][c] != -1:
                neighbors = [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]
                # Logic to filter valid neighbors within the grid and not obstacles
                valid_neighbors = [(nr, nc) for nr, nc in neighbors if 0 <= nr < rows and 0 <= nc < cols and grid.grid[nr][nc] != -1]

                for nr, nc in valid_neighbors:
                    # Assuming equal cost for moving to any neighboring cell
                    cost = 1
                    dp[nr][nc] = min(dp[nr][nc], dp[r][c] + cost)

    # Checking if the end point is reachable
    if dp[end[0]][end[1]] == float('inf'):
        print("No valid path found. Terminating the program.")
        sys.exit()
    
    # Reconstructing the optimal path using the dp table
    path = []
    r, c = end
    while (r, c) != start:
        path.append((r, c))
        neighbors = [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]
        # Logic to filter valid neighbors within the grid and not obstacles
        valid_neighbors = [(nr, nc) for nr, nc in neighbors if 0 <= nr < rows and 0 <= nc < cols and grid.grid[nr][nc] != -1]

        r, c = min(valid_neighbors, key=lambda x: dp[x[0]][x[1]])

    path.append(start)
    path.reverse()

    return path, dp[end[0]][end[1]]


# Method to visualize the grid with the optimal path
def visualize_path(grid, path):
    for r in range(grid.rows):
        for c in range(grid.cols):
            if (r, c) == grid.start:
                print("S ", end="")
            elif (r, c) == grid.end:
                print("E ", end="")
            elif grid.grid[r][c] == -1:
                print("# ", end="")
            elif (r, c) in path:
                print("* ", end="")
            else:
                print(". ", end="")
        print()

# Method to user interface to interactively set up the grid and find the optimal path
def terminal_interface():
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))

    grid = Grid(n, m)

    start_row = int(input("Enter the starting row: "))
    start_col = int(input("Enter the starting column: "))
    grid.set_start_point(start_row, start_col)

    end_row = int(input("Enter the ending row: "))
    end_col = int(input("Enter the ending column: "))
    grid.set_end_point(end_row, end_col)

    num_obstacles = int(input("Enter the number of obstacles: "))
    for _ in range(num_obstacles):
        obs_row = int(input("Enter obstacle row: "))
        obs_col = int(input("Enter obstacle column: "))
        grid.set_obstacle(obs_row, obs_col)

    # Visualizing the original grid
    print("\nOriginal Grid:")
    visualize_path(grid, [])
    
    # Finding the optimal path and its cost using dynamic programming
    path, min_cost = find_optimal_path(grid)  
    
    print(f"\nOptimal Path: {path}")
    print(f"Total Cost: {min_cost}")
    print("\nNew Grid:")

    # Visualizing the grid with the optimal path
    visualize_path(grid, path)

# Starting point of the code
if __name__ == "__main__":
    terminal_interface()
