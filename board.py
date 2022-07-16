import numpy as np, pygame
import random

class Board:

    def __init__(self, height, width,number_of_mines = 100) -> None:
        self.mouse_x = 1000
        self.mouse_y = 1000
        self.state = "Running"
        self.traversed = []
        self.flags = []
        self.height = height
        self.width = width
        self.color = [(120,120,120),(190,190,190)]
        self.rows = 25
        self.cols = 25
        self.grid = np.zeros((self.rows, self.cols))
        self.number_of_mines = number_of_mines
        self.__put_mines(self.number_of_mines)
        self.__numbers_next_to_mines()

    def draw_board(self, screen):
        font = pygame.font.Font(None,20)
        for i in range(self.cols):
            for j in range(self.rows):
                if (i,j) in self.traversed:
                    pygame.draw.rect(screen, self.color[1],(150 + i*20, 70 + j*20, 18, 18))
                    if self.grid[i][j] == 10:
                        text = pygame.image.load('src/mine.png')
                        text = pygame.transform.scale(text, (18,18))
                    else:
                        text = font.render(str(int(self.grid[i][j])), True, (0,120,0))
                    screen.blit(text, (152 + i*20,72 + j*20))
                elif (i,j) in self.flags:
                    pygame.draw.rect(screen, self.color[0],(150 + i*20, 70 + j*20, 18, 18))
                    flag = pygame.image.load('src/flag.png')
                    flag = pygame.transform.scale(flag, (18,18))
                    screen.blit(flag, (152 + i*20,72 + j*20))
                else:
                    pygame.draw.rect(screen, self.color[0],(150 + i*20, 70 + j*20, 18, 18))

    def __put_mines(self, number_of_mines):
        for i in range(number_of_mines):
            random_col = random.randint(0,self.cols-1)
            random_row = random.randint(0,self.rows-1)
            self.grid[random_row][random_col] = 10

    def draw_mine(self, screen):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 10:
                    pygame.draw.rect(screen, (255,0,0), (150 + j*20, 70 + i*20, 18, 18))
        
        pygame.display.update()

    def __numbers_next_to_mines(self):
        
        for i in range(self.rows):
            for j in range(self.cols):
                self.__check_block(i, j)

    def __check_block(self, i, j):
        if self.grid[i][j] == 10:
            pass
        else:
            try:
                if i-1>=0:
                    if self.grid[i-1][j] == 10:
                        self.grid[i][j] += 1
            except:
                pass
            try:
                if i+1 < self.rows:
                    if self.grid[i+1][j] == 10:
                        self.grid[i][j] += 1
            except:
                pass
            try:
                if i-1>=0 and j-1>=0:
                    if self.grid[i-1][j-1] == 10:
                        self.grid[i][j] += 1
            except:
                pass
            try:
                if i-1>=0 and j+1 < self.rows:
                    if self.grid[i-1][j+1] == 10:
                        self.grid[i][j] += 1
            except:
                pass
            try:
                if j-1>=0:
                    if self.grid[i][j-1] == 10:
                        self.grid[i][j] += 1
            except:
                pass
            try:
                if self.grid[i][j+1] == 10:
                    self.grid[i][j] += 1
            except:
                pass
            try:
                if i+1< self.rows and j-1>=0:
                    if self.grid[i+1][j-1] == 10:
                        self.grid[i][j] += 1
            except:
                pass
            try:
                if i+1< self.rows and j+1<self.cols:
                    if self.grid[i+1][j+1] == 10:
                        self.grid[i][j] += 1
            except:
                pass

    def chosen(self, i, j):
        if (i, j) not in self.traversed:
            self.mouse_x = i
            self.mouse_y = j
            if self.grid[i][j] == 10:
                self.state = "Game Over"
            else:
                self.traverse(i,j)
    
    def traverse(self, i, j):

        if (i, j) not in self.traversed:
            try:
                if self.grid[i][j] == 0:
                    self.traversed.append((i,j))

                    if i> 0:
                        self.traverse(i-1, j)
                    if i< self.rows:
                        self.traverse(i+1, j)
                    if j>0:
                        self.traverse(i, j-1)
                    if j< self.cols:
                        self.traverse(i, j+1)
                    if i>0 and j> 0:
                        self.traverse(i-1, j-1)
                    if i>0 and j< self.cols - 1:
                        self.traverse(i-1, j+1)
                    if i< self.rows - 1 and j>0:
                        self.traverse(i+1, j-1)
                    if i< self.rows - 1 and j < self.cols - 1:
                        self.traverse(i+1, j+1)

                else:
                    self.traversed.append((i,j))
            
            except:
                pass

    def draw_board_over(self, screen):
        font = pygame.font.Font(None,20)
        for i in range(self.cols):
            for j in range(self.rows):
                if (i,j) == (self.mouse_x, self.mouse_y):
                   pygame.draw.rect(screen, (255,0,0),(150 + i*20, 70 + j*20, 18, 18)) 
                else:
                    pygame.draw.rect(screen, self.color[1],(150 + i*20, 70 + j*20, 18, 18))
                if self.grid[i][j] == 10:
                    text = pygame.image.load('src/mine.png')
                    text = pygame.transform.scale(text, (18,18))
                else:
                    text = font.render(str(int(self.grid[i][j])), True, (0,120,0))
                screen.blit(text, (150 + i*20,70 + j*20))
                if (i,j) in self.flags:
                    pygame.draw.rect(screen, self.color[0],(150 + i*20, 70 + j*20, 18, 18))
                    flag = pygame.image.load('src/flag.png')
                    flag = pygame.transform.scale(flag, (18,18))
                    screen.blit(flag, (152 + i*20,72 + j*20))

    def flagged(self, i, j):
        self.flags.append((i,j))

        

        

                    
                

