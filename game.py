import pygame
from board import Board


def main():
    ##### INITIALIZE PYGAME ######
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    running = True
    ##### SET ICON AND TITLE #####
    pygame.display.set_caption("Minesweeper")
    icon = pygame.image.load('src/mine.png')
    pygame.display.set_icon(icon)
    #### Initialize the game #####
    game = Board(500, 700)
    a = None
    while running:

        screen.fill((255,255,255))
        if game.state == "Running":
            game.draw_board(screen)

            for event in pygame.event.get():
                ## QUIT CONDITION
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x,y = pygame.mouse.get_pos()
                        game.chosen((x-150)//20,(y-70)//20)
                    if event.button == 3:
                        x,y = pygame.mouse.get_pos()
                        game.flagged((x-150)//20,(y-70)//20)

            ## Update the screen after every iteration
            pygame.display.update()
        if game.state == "Game Over":

            screen.fill((255,255,255))
            game.draw_board_over(screen)

            for event in pygame.event.get():
                ## QUIT CONDITION
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()
    ## Close the pygame engine
    pygame.quit()

if __name__ == "__main__":
    main()