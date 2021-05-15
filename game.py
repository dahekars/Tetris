import pygame
import random

pygame.init()

#windows details 
    ## windows size
window_width = 800
window_height = 700
    ## play_area
play_area_width = 300
play_area_height = 600
block_size = 30

top_left_x = (window_width - play_area_width) // 2
top_left_y = (window_height - play_area_height)

#Shapes for game

S = [[".....",
      ".....",
      "..00.",
      ".00..",
      "....."],
     [".....",
      "..0..",
      "..00.",
      "...0.", 
      "....."]]

Z = [[".....",
      ".....",
      ".00..",
      "..00.",
      "....."],
     [".....",
      "..0..",
      ".00..",
      ".0...",
      "....."]]

I = [["..0..",
      "..0..",
      "..0..",
      "..0..",
      "....."],
     [".....",
      ".....",
      "0000.",
      ".....",
      "....."]]

O = [[".....", 
      ".....",
      "..00.",
      "..00.",
      "....."]]

J = [[".....", 
      "..0..",
      "..0..",
      ".00..",
      "....."],
     [".....",
      ".0...",
      ".000.",
      ".....",
      "....."],
     [".....",
      "..00.",
      "..0..",
      "..0..",
      "....."],
     [".....",
      ".000.",
      "...0.",
      ".....",
      "....."]]

L = [[".....",
      "..0..",
      "..0..",
      "..00.",
      "....."],
     [".....",
      ".000.",
      ".0...",
      ".....",
      "....."],
     [".....",
      ".00..",
      "..0..",
      "..0..",
      "....."],
     [".....",
      "...0.",
      ".000.",
      ".....", 
      "...."]]

T = [[".....",
      ".000.", 
      "..0..",
      ".....",
      "....."],
     [".....",
      "...0.",
      "..00.",
      "...0.",
      "....."],
     [".....",
      "..0..",
      ".000.",
      ".....",
      "....."],
     [".....",
      ".0...",
      ".00..",
      ".0...",
      "....."]]

Shapes = [S,Z,I,O,J,L,T]

#Colors

red = (255,0,0)
blue = (65,105,225)
green = (0,128,0)
orange = (255,165,0)
maroon = (128,0,0)
violet = (148,0,211)
chocolate = (210,105,30)
black = (0,0,0)
gold = 	(255,215,0)

color = [red,blue,green,orange, black, maroon, violet, chocolate]

#code details
class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color[Shapes.index(shape)]
        self.rotation = 0

def grid(locked_pos = {}): # get inther play area of program
    grid = [[(0,0,0) for _ in range(10)]for _ in range(20)]
    
    for rows in range(grid):
        for colms in range(grid(rows)):
            if (colms, rows) in locked_pos:
                c = locked_pos[(colms, rows)]
                grid[rows][colms] = c
    return grid

def get_shape(): #get shape working
    return Piece(5, 0, random.choice(Shapes))

def draw_grid(surface, grid):
    surface.fill(black)

    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 50)
    label = font.render("Tetris", True, (255,255,255))
    
    surface.blit(label, (top_left_x + play_area_width/2 -(label.get_width()/2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j],(top_left_x + j*block_size, top_left_y+i*block_size, block_size, block_size), 0)


    pygame.draw.rect(surface, red, (top_left_x,top_left_y, play_area_width, play_area_height), 4)
     
    pygame.display.update()

def draw_window(surface,grid):
    surface.fill(black)

    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 50)
    label = font.render("Tetris", True, (255,255,255))
    
    surface.blit(label, (top_left_x + play_area_width/2 -(label.get_width()/2), 30))
    pygame.display.update()

    draw_grid(surface, grid)

def main():

    locked_pos = {}
    grid = grid(locked_pos)
    change_piece = False
    current_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.rotation -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x -= 1