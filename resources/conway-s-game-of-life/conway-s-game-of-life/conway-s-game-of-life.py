import matplotlib.pyplot as plt

class GameOfLife(object):
    """
    A class to represent Conway's Game of Life.
    
    Attributes:
    -----------
    x_dim : int
        Number of rows in the grid.
    y_dim : int
        Number of columns in the grid.
    grid : list of list of int
        2D grid representing the current state of the game, where 0 indicates a dead cell
        and 1 indicates a live cell.
    """
    
    def __init__(self, x_dim, y_dim):
        """
        Initialize the game grid with the specified dimensions.
        
        Parameters:
        -----------
        x_dim : int
            Number of rows in the grid.
        y_dim : int
            Number of columns in the grid.
        """
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.grid = [[0 for _ in range(y_dim)] for _ in range(x_dim)]
    
    def get_grid(self):
        """
        Get the current state of the game grid.
        
        Returns:
        --------
        list of list of int
            The current state of the grid.
        """
        return self.grid
    
    def print_grid(self):
        for row in self.grid:
            for cell in row:
                print(cell, end=' ')
            print()
            print('-' * (self.y_dim * 2))
    
    def populate_grid(self, coord):
        """
        Populate the grid with live cells at the given coordinates.
        
        Parameters:
        -----------
        coord : list of tuple of int
            A list of tuples, where each tuple contains the (row, column) coordinates
            of a cell to be set as alive.
        
        Returns:
        --------
        None
        """
        for (row, col) in coord:
            if 0 <= row < self.x_dim and 0 <= col < self.y_dim:
                self.grid[row][col] = 1
        return self.grid
    
    def make_step(self):
        """
        Perform a single iteration of the Game of Life.
        
        Returns:
        --------
        None
        """
        sum_grid = [[0 for _ in range(self.y_dim)] for _ in range(self.x_dim)]
        
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                for a in range(max(0, i-1), min(self.x_dim, i+2)):
                    for b in range(max(0, j-1), min(self.y_dim, j+2)):
                        if (a, b) != (i, j):
                            sum_grid[i][j] += self.grid[a][b]
        
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                if self.grid[i][j] == 1:
                    if sum_grid[i][j] < 2 or sum_grid[i][j] > 3:
                        self.grid[i][j] = 0
                else:
                    if sum_grid[i][j] == 3:
                        self.grid[i][j] = 1
        
        return self.grid
    
    def make_n_steps(self, n):
        """
        Simulate multiple iterations of the Game of Life.
        
        Parameters:
        -----------
        n : int
            The number of steps to simulate.
        
        Returns:
        --------
        None
        """
        for _ in range(n):
            self.make_step()
        return self.grid
    
    def draw_grid(self):
        x = []
        y = []

        # Collect the coordinates of live cells
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                if self.grid[i][j] == 1:
                    x.append(j)
                    y.append(i)

        # Initialize the plot
        fig, ax = plt.subplots(figsize=(6, 6))

        # Draw the scatter plot
        ax.scatter(x, y, c='black', marker='s', s=100)

        # Set the limits and invert y-axis to match the printed grid's orientation
        ax.set_xlim(0, self.y_dim)
        ax.set_ylim(0, self.x_dim)
        ax.invert_yaxis()

        # Hide the axis ticks
        ax.set_xticks([])
        ax.set_yticks([])

        plt.show()

# Test the draw_grid method
game = GameOfLife(10, 10)
game.populate_grid([(1, 1), (1, 2), (1, 3), (2, 2), (3, 3), (4, 4)])
game.draw_grid()



