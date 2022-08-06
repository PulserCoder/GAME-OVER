import pygame
import time

colors = {
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'BLUE': (0, 0, 255),
    'GREEN': (0, 255, 0),
    'WHITE': (239, 239, 239),
    'YELlOW': (255, 255, 0)
}


class Block():
    def __init__(self, x, y, w, h, color, srceen):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.color = color
        self.screen = srceen

    def update(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))


class Player():
    def __init__(self, color, screen):
        self.color = color
        self.screen = screen


    def update(self, position_x, position_y):
        pygame.draw.rect(self.screen, self.color, (position_x, position_y, 13, 13))


if __name__ == '__main__':

    pygame.init()

    size = width, height = 1000, 1000

    screen = pygame.display.set_mode(size)
    die_flag = True
    win_flag = False
    running = True
    x_pos = 0
    clock = pygame.time.Clock()
    die_coord_level1 = [

        (600, 275, 90, 110),
        (200, 0, 10, 50),
        (200, 100, 10, 100),
        (0, 200, 210, 10),
        (200, 40, 200, 10),
        (400, 0, 10, 50),
        (400, 0, 200, 10),
        (200, 100, 260, 10),
        (450, 30, 10, 70),
        (450, 30, 110, 10),
        (200, 0, 10, 50),
        (200, 100, 10, 100),
        (0, 200, 210, 10),
        (200, 40, 200, 10),
        (400, 0, 10, 50),
        (400, 0, 400, 10),
        (200, 100, 260, 10),
        (450, 30, 10, 70),
        (450, 30, 320, 10),
        (800, 0, 10, 350),
        (770, 30, 10, 360),
        (770, 380, 100, 10),
        (800, 350, 30, 10),
        (830, 210, 10, 150),
        (870, 240, 10, 150),
        (830, 210, 150, 10),
        (870, 240, 75, 10),
        (980, 210, 10, 450),
        (940, 240, 10, 350),
        (200, 0, 10, 50),
        (200, 100, 10, 100),
        (0, 200, 210, 10),
        (200, 40, 200, 10),
        (400, 0, 10, 50),
        (400, 0, 400, 10),
        (200, 100, 260, 10),
        (450, 30, 10, 70),
        (450, 30, 320, 10),
        (800, 0, 10, 350),
        (770, 30, 10, 360),
        (770, 380, 100, 10),
        (800, 350, 30, 10),
        (830, 210, 10, 150),
        (870, 240, 10, 150),
        (830, 210, 150, 10),
        (870, 240, 75, 10),
        (980, 210, 10, 450),
        (940, 240, 10, 350),
        (380, 650, 600, 10),
        (430, 590, 520, 10),
        (380, 450, 10, 210),
        (200, 0, 10, 50),
        (200, 100, 10, 100),
        (0, 200, 210, 10),
        (200, 40, 200, 10),
        (400, 0, 10, 50),
        (400, 0, 400, 10),
        (200, 100, 260, 10),
        (450, 30, 10, 70),
        (450, 30, 320, 10),
        (800, 0, 10, 350),
        (770, 30, 10, 360),
        (770, 380, 100, 10),
        (800, 350, 30, 10),
        (830, 210, 10, 150),
        (870, 240, 10, 150),
        (830, 210, 150, 10),
        (870, 240, 75, 10),
        (980, 210, 10, 450),
        (940, 240, 10, 350),
        (380, 650, 600, 10),
        (430, 590, 520, 10),
        (380, 450, 10, 210),
        (430, 400, 10, 190),
        (170, 400, 260, 10),
        (240, 450, 150, 10),
        (170, 400, 10, 400),
        (240, 450, 10, 280),
        (170, 800, 215, 10),
        (240, 730, 160, 10),
        (400, 730, 10, 150),
        (375, 800, 10, 80),
        (275, 870, 10, 150),
        (275, 870, 100, 10),
        (375, 800, 10, 80),
        (275, 870, 10, 150),
        (275, 870, 100, 10),
        (410, 870, 100, 10),
        (510, 870, 10, 150),

        # (10, 150, 250, 10),
        # (30, 80, 120, 10)
    ]
    blocklist_level1 = [
        Block(285, 880, 225, 120,  colors['GREEN'], screen),
        Block(200, 0, 10, 50, colors['WHITE'], screen),
        Block(200, 100, 10, 100, colors['WHITE'], screen),
        Block(0, 200, 210, 10, colors['WHITE'], screen),
        Block(200, 40, 200, 10, colors['WHITE'], screen),
        Block(400, 0, 10, 50, colors['WHITE'], screen),
        Block(400, 0, 200, 10, colors['WHITE'], screen),
        Block(200, 100, 260, 10, colors['WHITE'], screen),
        Block(450, 30, 10, 70, colors['WHITE'], screen),
        Block(450, 30, 110, 10, colors['WHITE'], screen),
        Block(200, 0, 10, 50, colors['WHITE'], screen),
        Block(200, 100, 10, 100, colors['WHITE'], screen),
        Block(0, 200, 210, 10, colors['WHITE'], screen),
        Block(200, 40, 200, 10, colors['WHITE'], screen),
        Block(400, 0, 10, 50, colors['WHITE'], screen),
        Block(400, 0, 400, 10, colors['WHITE'], screen),
        Block(200, 100, 260, 10, colors['WHITE'], screen),
        Block(450, 30, 10, 70, colors['WHITE'], screen),
        Block(450, 30, 320, 10, colors['WHITE'], screen),
        Block(800, 0, 10, 350, colors['WHITE'], screen),
        Block(770, 30, 10, 360, colors['WHITE'], screen),
        Block(770, 380, 100, 10, colors['WHITE'], screen),
        Block(800, 350, 30, 10, colors['WHITE'], screen),
        Block(830, 210, 10, 150, colors['WHITE'], screen),
        Block(870, 240, 10, 150, colors['WHITE'], screen),
        Block(830, 210, 150, 10, colors['WHITE'], screen),
        Block(870, 240, 75, 10, colors['WHITE'], screen),
        Block(980, 210, 10, 450, colors['WHITE'], screen),
        Block(940, 240, 10, 350, colors['WHITE'], screen),
        Block(200, 0, 10, 50, colors['WHITE'], screen),
        Block(200, 100, 10, 100, colors['WHITE'], screen),
        Block(0, 200, 210, 10, colors['WHITE'], screen),
        Block(200, 40, 200, 10, colors['WHITE'], screen),
        Block(400, 0, 10, 50, colors['WHITE'], screen),
        Block(400, 0, 400, 10, colors['WHITE'], screen),
        Block(200, 100, 260, 10, colors['WHITE'], screen),
        Block(450, 30, 10, 70, colors['WHITE'], screen),
        Block(450, 30, 320, 10, colors['WHITE'], screen),
        Block(800, 0, 10, 350, colors['WHITE'], screen),
        Block(770, 30, 10, 360, colors['WHITE'], screen),
        Block(770, 380, 100, 10, colors['WHITE'], screen),
        Block(800, 350, 30, 10, colors['WHITE'], screen),
        Block(830, 210, 10, 150, colors['WHITE'], screen),
        Block(870, 240, 10, 150, colors['WHITE'], screen),
        Block(830, 210, 150, 10, colors['WHITE'], screen),
        Block(870, 240, 75, 10, colors['WHITE'], screen),
        Block(980, 210, 10, 450, colors['WHITE'], screen),
        Block(940, 240, 10, 350, colors['WHITE'], screen),
        Block(380, 650, 600, 10, colors['WHITE'], screen),
        Block(430, 590, 520, 10, colors['WHITE'], screen),
        Block(380, 450, 10, 210, colors['WHITE'], screen),
        Block(200, 0, 10, 50, colors['WHITE'], screen),
        Block(200, 100, 10, 100, colors['WHITE'], screen),
        Block(0, 200, 210, 10, colors['WHITE'], screen),
        Block(200, 40, 200, 10, colors['WHITE'], screen),
        Block(400, 0, 10, 50, colors['WHITE'], screen),
        Block(400, 0, 400, 10, colors['WHITE'], screen),
        Block(200, 100, 260, 10, colors['WHITE'], screen),
        Block(450, 30, 10, 70, colors['WHITE'], screen),
        Block(450, 30, 320, 10, colors['WHITE'], screen),
        Block(800, 0, 10, 350, colors['WHITE'], screen),
        Block(770, 30, 10, 360, colors['WHITE'], screen),
        Block(770, 380, 100, 10, colors['WHITE'], screen),
        Block(800, 350, 30, 10, colors['WHITE'], screen),
        Block(830, 210, 10, 150, colors['WHITE'], screen),
        Block(870, 240, 10, 150, colors['WHITE'], screen),
        Block(830, 210, 150, 10, colors['WHITE'], screen),
        Block(870, 240, 75, 10, colors['WHITE'], screen),
        Block(980, 210, 10, 450, colors['WHITE'], screen),
        Block(940, 240, 10, 350, colors['WHITE'], screen),
        Block(380, 650, 600, 10, colors['WHITE'], screen),
        Block(430, 590, 520, 10, colors['WHITE'], screen),
        Block(380, 450, 10, 210, colors['WHITE'], screen),
        Block(430, 400, 10, 190, colors['WHITE'], screen),
        Block(170, 400, 260, 10, colors['WHITE'], screen),
        Block(240, 450, 150, 10, colors['WHITE'], screen),
        Block(170, 400, 10, 400, colors['WHITE'], screen),
        Block(240, 450, 10, 280, colors['WHITE'], screen),
        Block(170, 800, 215, 10, colors['WHITE'], screen),
        Block(240, 730, 160, 10, colors['WHITE'], screen),
        Block(400, 730, 10, 150, colors['WHITE'], screen),
        Block(375, 800, 10, 80, colors['WHITE'], screen),
        Block(275, 870, 10, 150, colors['WHITE'], screen),
        Block(275, 870, 100, 10, colors['WHITE'], screen),
        Block(375, 800, 10, 80, colors['WHITE'], screen),
        Block(275, 870, 10, 150, colors['WHITE'], screen),
        Block(275, 870, 100, 10, colors['WHITE'], screen),
        Block(410, 870, 100, 10, colors['WHITE'], screen),
        Block(510, 870, 10, 150, colors['WHITE'], screen),

    ]
    blocklist_level2 = [
        Block(0, 200, 210, 10, colors['WHITE'], screen),
        Block(200, 0, 10, 150, colors['WHITE'], screen),
        Block(200, 200, 250, 10, colors['WHITE'], screen),
        Block(200, 150, 300, 10, colors['WHITE'], screen),
        Block(450, 200, 10, 150, colors['WHITE'], screen),
        Block(500, 150, 10, 200, colors['WHITE'], screen),
        Block(0, 200, 210, 10, colors['WHITE'], screen),
        Block(200, 0, 10, 150, colors['WHITE'], screen),
        Block(200, 200, 250, 10, colors['WHITE'], screen),
        Block(200, 150, 300, 10, colors['WHITE'], screen),
        Block(450, 200, 10, 150, colors['WHITE'], screen),
        Block(500, 150, 10, 200, colors['WHITE'], screen),
        Block(50, 350, 410, 10, colors['WHITE'], screen),
        Block(500, 350, 410, 10, colors['WHITE'], screen),
        Block(910, 350, 10, 200, colors['WHITE'], screen),
        Block(870, 400, 10, 200, colors['WHITE'], screen),
        Block(870, 600, 70, 10, colors['WHITE'], screen),
        Block(0, 200, 210, 10, colors['WHITE'], screen),
        Block(200, 0, 10, 150, colors['WHITE'], screen),
        Block(200, 200, 250, 10, colors['WHITE'], screen),
        Block(200, 150, 300, 10, colors['WHITE'], screen),
        Block(450, 200, 10, 150, colors['WHITE'], screen),
        Block(500, 150, 10, 200, colors['WHITE'], screen),
        Block(50, 350, 410, 10, colors['WHITE'], screen),
        Block(500, 350, 410, 10, colors['WHITE'], screen),
        Block(910, 350, 10, 200, colors['WHITE'], screen),
        Block(870, 400, 10, 200, colors['WHITE'], screen),
        Block(870, 600, 80, 10, colors['WHITE'], screen),
        Block(910, 550, 70, 10, colors['WHITE'], screen),
        Block(970, 550, 10, 300, colors['WHITE'], screen),
        Block(940, 600, 10, 250, colors['WHITE'], screen),
        Block(970, 850, 50, 10, colors['WHITE'], screen),
        Block(850, 850, 100, 10, colors['WHITE'], screen),
        Block(850, 850, 100, 10, colors['WHITE'], screen),
        Block(850, 850, 10, 400, colors['WHITE'], screen)

    ]
    die_coord_level2 = [
        (0, 200, 210, 10),
        (200, 0, 10, 150),
        (200, 200, 250, 10),
        (200, 150, 300, 10),
        (450, 200, 10, 150),
        (500, 150, 10, 200),
        (0, 200, 210, 10),
        (200, 0, 10, 150),
        (200, 200, 250, 10),
        (200, 150, 300, 10),
        (450, 200, 10, 150),
        (500, 150, 10, 200),
        (50, 350, 410, 10),
        (500, 350, 410, 10),
        (910, 350, 10, 200),
        (870, 400, 10, 200),
        (870, 600, 70, 10),
        (0, 200, 210, 10),
        (200, 0, 10, 150),
        (200, 200, 250, 10),
        (200, 150, 300, 10),
        (450, 200, 10, 150),
        (500, 150, 10, 200),
        (50, 350, 410, 10),
        (500, 350, 410, 10),
        (910, 350, 10, 200),
        (870, 400, 10, 200),
        (870, 600, 80, 10),
        (910, 550, 70, 10),
        (970, 550, 10, 300),
        (940, 600, 10, 250),
        (970, 850, 50, 10),
        (850, 850, 100, 10),
        (850, 850, 100, 10),
        (850, 850, 10, 400)

    ]
    win_coord_level2 = [

    ]
    win_coord_level1 = [
        (285, 880, 225, 120)
    ]
    player = Player(colors['YELlOW'], screen)
    die_image = pygame.image.load('die_background.png')
    die_rect = die_image.get_rect(
        bottomright=(1000, 1000))
    win_image = pygame.image.load('win1.png')
    win_rect = win_image.get_rect(
        bottomright=(1000, 1000))
    pygame.display.set_caption('GAME OVER.')
    level2 = False
    while running:
        if die_flag:
            screen.blit(die_image, die_rect)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEMOTION:
                    x = event.pos[0]
                    y = event.pos[1]
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if (x >= 0 and x <= 180) and (
                                y >= 0 and y <= 180):
                            die_flag = False
        elif win_flag:
            screen.blit(win_image, win_rect)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        level2 = True
                        die_flag = True
                        win_flag = False
        elif level2:
            screen.fill(colors['BLUE'])
            for i in blocklist_level2:
                i.update()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        print("Hey, you pressed the key, '0'!")

                if event.type == pygame.MOUSEMOTION:
                    # pygame.draw.circle(screen, (0, 0, 255), event.pos, 10)
                    x_y = event.pos
                    player.update(x_y[0], x_y[1])
                    for coord in die_coord_level2:
                        x = x_y[0]
                        y = x_y[1]
                        if (x >= coord[0] and x <= coord[0] + coord[2]) and (y >= coord[1] and y <= coord[1] + coord[3]):
                            die_flag = True
                    for i in win_coord_level2:
                        x = x_y[0]
                        y = x_y[1]
                        if (x >= i[0] and x <= i[0] + i[2]) and (y >= i[1] and y <= i[1] + i[3]):
                            win_flag = True

        else:
            screen.fill(colors['BLUE'])
            for i in blocklist_level1:
                i.update()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        print("Hey, you pressed the key, '0'!")

                if event.type == pygame.MOUSEMOTION:
                    # pygame.draw.circle(screen, (0, 0, 255), event.pos, 10)
                    x_y = event.pos
                    player.update(x_y[0], x_y[1])
                    for coord in die_coord_level1:
                        x = x_y[0]
                        y = x_y[1]
                        if (x >= coord[0] and x <= coord[0] + coord[2]) and (y >= coord[1] and y <= coord[1] + coord[3]):
                            die_flag = True
                    for i in win_coord_level1:
                        x = x_y[0]
                        y = x_y[1]
                        if (x >= i[0] and x <= i[0] + i[2]) and (y >= i[1] and y <= i[1] + i[3]):
                            win_flag = True


        pygame.display.flip()

        clock.tick(50)

        # отрисовка и изменение свойств объектов

    pygame.quit()
