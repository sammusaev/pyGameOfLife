import  pygame as pg, numpy as np

class Grid:
    def __init__(self, width, height, cell, margin):
        self.cell   = cell
        self.cols   = int(height/(cell+margin))
        self.rows   = int(width/(cell+margin))
        self.size   = (self.rows, self.cols)
        self.margin = margin
        self.running= False
        self.saved_state = [] #implement ability to store multiple grids

    def toggle_running(self):
        if self.running: self.running = False
        else: self.running = True
    
    def save_state(self):
        self.saved_state = []
        self.saved_state.append(self.grid)

    def load_state(self):
        if len(self.saved_state)>0: #implement ability to store multiple grids
            self.grid = self.saved_state[0]
    
    def generate_grid(self, ratio, isRandom):
        if isRandom: self.grid = np.random.choice([0,1], size=self.size, p=ratio)
        else: self.grid = np.zeros(shape=(self.size))
    
    def insert_coord(self, rowIdx, colIdx):
        if self.grid[rowIdx,colIdx] == 1: self.grid[rowIdx,colIdx] = 0
        else: self.grid[rowIdx,colIdx] = 1

    def get_neighbors(self, cellIdx):
        neighbors = 0
        for i in range(-1,2):
            for j in range(-1,2):
                x_edge = (cellIdx[0]+i+self.rows)%self.rows
                y_edge = (cellIdx[1]+j+self.cols)%self.cols
                neighbors += self.grid[x_edge,y_edge]
        neighbors-=self.grid[cellIdx[0], cellIdx[1]] #since current cell can't be a member
        return neighbors

    def determine_if_lives(self, cellIdx, neighbors):
        neighbors = self.get_neighbors(cellIdx)

        #if alive and 2-3 live neighbors
        if self.grid[cellIdx]==1 and (neighbors==2 or neighbors==3): return True
        
        #if dead and 3 live neighbors
        elif self.grid[cellIdx]==0 and neighbors==3: return True

        return False

    def draw_grid(self, color_on, color_off, surface):
        for x in range(self.rows):
            for y in range(self.cols):
                if self.grid[x,y]==1: 
                    color = color_on
                else:
                    color = color_off
                pg.draw.rect(surface, color, 
                [(self.margin+self.cell)*y+self.margin,
                (self.margin+self.cell)*x+self.margin,
                self.cell, self.cell])

        next_grid = np.ndarray(shape=(self.size)) #manipulating current would not work

        if (self.running):
            for x in range(self.rows):
                for y in range(self.cols):
                    current_neighbors = self.get_neighbors((x,y))
                    lives = self.determine_if_lives((x,y), current_neighbors)
                    if lives: 
                        next_grid[x,y] = 1
                    else:
                        next_grid[x,y] = 0
            self.grid = next_grid
