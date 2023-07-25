import time

from game_settings import *
from solver import Solver
from table import Table

WINDOW = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Sameer's A* puzzle game")


def main():
    run = True
    clock = pygame.time.Clock()

    numberOfBoxes = 3  # Determining number of rows and cols
    table = Table(numberOfBoxes, WINDOW)  # Table board class

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    table.draw(WINDOW)
                elif event.key == pygame.K_DOWN:
                    table.move("down")
                    table.draw(WINDOW)
                elif event.key == pygame.K_UP:
                    table.move("up")
                    table.draw(WINDOW)
                elif event.key == pygame.K_RIGHT:
                    table.move("right")
                    table.draw(WINDOW)
                elif event.key == pygame.K_LEFT:
                    table.move("left")
                    table.draw(WINDOW)
                elif event.key == pygame.K_a:
                    solver = Solver(table)
                    path = solver.solve()
                    for move in path:
                        table.move(move)
                        table.draw(WINDOW)
                        pygame.display.update()
                        time.sleep(0.2)
                    print("Solved successfully")
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
