import os, math, grid, pygame as pg

SCREEN_WIDTH = 800
SCREEN_HEIGHT= 800

FPS = 60

CELL_MARGIN = 1 

#Stupidty right off the bat
CELL = SCREEN_WIDTH/80 - CELL_MARGIN

#Probability of generating [dead,live] cells
RATIO = [0.9, 0.1]

COLOR_SURFACE = (69,69,69) #the margin/bg
COLOR_OFF     = (40,40,40) #dead
COLOR_ON      = (255,160,122)#live

def main():
    pg.init()
    pg.display.set_caption("pyGame of Life")

    SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    CLOCK = pg.time.Clock()

    GRID = grid.Grid(SCREEN_WIDTH,SCREEN_HEIGHT,CELL,CELL_MARGIN)
    GRID.generate_grid(RATIO, False)

    run = True
    while run:
        CLOCK.tick(FPS)
        SCREEN.fill(COLOR_SURFACE)

        for event in pg.event.get():
            if event.type == pg.QUIT: 
                run = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    run = False
                if event.key == pg.K_r:
                    GRID.generate_grid(RATIO, True)
                if event.key == pg.K_n:
                    GRID.generate_grid(RATIO, False)
                if event.key == pg.K_SPACE:
                    GRID.toggle_running()
                if event.key == pg.K_s:
                    GRID.save_state()
                if event.key == pg.K_l:
                    GRID.load_state()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                col_idx = math.floor(mouse_pos[0]/(CELL+CELL_MARGIN))
                row_idx = math.floor(mouse_pos[1]/(CELL+CELL_MARGIN))
                GRID.insert_coord(row_idx,col_idx)

        GRID.draw_grid(COLOR_ON, COLOR_OFF, SCREEN)

        pg.display.update() 

if __name__ == "__main__":
    main()
