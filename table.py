from random import sample
from game_settings import *


class Box:  # box class in table
    def __init__(self, val, x, y, w, h, axis):
        self.val = val
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.axis = axis

    def drawBox(self, window):
        if self.val == 0:
            pygame.draw.rect(window, (69, 85, 89),
                             (self.x, self.y, self.w, self.h),
                             border_radius=100)
        else:
            pygame.draw.rect(window, boxColor,
                             (self.x, self.y, self.w, self.h),
                             border_radius=100)
            numberText = numberFont.render(self.val.__str__(), True, (255, 255, 255))
            window.blit(numberText, (self.x + (self.w / 2) - (numberText.get_width() / 2),
                                     self.y + (self.h / 2) - (numberText.get_height() / 2)))


class Table:
    def __init__(self, n, window):

        pygame.draw.rect(window, gameBgColor, (0, 0, WIDTH, HEIGHT))
        titleText = font1.render("<< This is Sameer A* puzzle >>", 100, (255, 0, 0))
        window.blit(titleText, ((WIDTH - titleText.get_width()) / 2, 10))
        text2 = font2.render("Press \"s\" to play", True, (255, 255, 255))
        window.blit(text2, ((500 - text2.get_width()) / 2, (HEIGHT / 2) - text2.get_height()))
        text3 = font2.render("If u want to solve the puzzle automatically", True, (0, 245, 0))
        window.blit(text3, ((500 - text3.get_width()) / 2, (HEIGHT / 2) + 30 - text3.get_height()))
        text4 = font2.render("Press \"a\"", True, (0, 245, 0))
        window.blit(text4, ((500 - text4.get_width()) / 2, (HEIGHT / 2) + 60 - text4.get_height()))

        self.MOVE_KEYS = {
            "up": (-1, 0),
            "down": (1, 0),
            "right": (0, 1),
            "left": (0, -1)
        }

        self.n = n
        newHeight = HEIGHT - titleHeight - ((n + 1) * 10)
        newWidth = WIDTH - ((n + 1) * 10)
        verticalSpace = titleHeight + 10
        horizontalSpace = 10
        self.boxes = []
        val = 0
        for row in range(n):
            self.boxes.append([])
            for col in range(n):
                self.boxes[row].append(
                    Box(val, horizontalSpace, verticalSpace, (newWidth / n), (newHeight / n), (row, col)))
                val = val + 1
                horizontalSpace = horizontalSpace + (newWidth / n) + 10
            horizontalSpace = 10
            verticalSpace = verticalSpace + (newHeight / n) + 10

        all_pos = list(self.MOVE_KEYS.keys())
        for shift in range(1000):
            move = sample(all_pos, 1)[0]
            self.move(move)

    def draw(self, window):
        pygame.draw.rect(window, gameBgColor, (0, 50, WIDTH, HEIGHT))

        for row in range(self.n):
            for col in range(self.n):
                self.boxes[row][col].drawBox(window)

    def move(self, move):

        if move not in self.MOVE_KEYS:
            return False

        for row in range(self.n):
            for col in range(self.n):
                if self.boxes[row][col].val == 0:
                    zeroPos = self.boxes[row][col].axis

        zeroRow, zeroCol = zeroPos
        newRow = zeroRow + self.MOVE_KEYS[move][0]
        newCol = zeroCol + self.MOVE_KEYS[move][1]

        if newRow < 0 or newCol < 0 or newCol >= self.n or newRow >= self.n:
            return False
        else:
            self.boxes[zeroRow][zeroCol].val = self.boxes[newRow][newCol].val
            self.boxes[newRow][newCol].val = 0
            return True
