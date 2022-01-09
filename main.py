import pygame
import sys
import os

theme_list = ['Цветочная']
theme_num = 0
theme = theme_list[theme_num]
speed_list = [30, 60, 90, 120]
durability_list = [1, 2, 4, 6]
amount_list = [5, 8, 10]
speed_num = 0
durability_num = 0
amount_num = 0
speed = speed_list[speed_num]
durability = durability_list[durability_num]
amount = amount_list[amount_num]
vertical_borders = pygame.sprite.Group()


def set_parameters(theme_par, speed_par, durability_par, amount_par):
    if theme_par == '':
        pass
    if speed_par == '':
        pass
    if durability_par == '':
        pass
    if amount_par == '':
        pass


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    '''if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()'''
    return image


def draw(x, y, w, h, clr, txt):
    font = pygame.font.SysFont("gabriola", 50)
    text = font.render(txt, True, clr)
    screen.blit(text, (x, y))
    pygame.draw.rect(screen, clr, (x - 10, y - 10, w + 20, h + 20), 1)


def button(x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    if (x + w > int(mouse[0]) > x) and (y + h > int(mouse[1]) > y):
        if action == 'start':
            draw(x, y, w, h, ac, 'Начать')
        elif action == 'exit':
            draw(x, y, w, h, ac, 'Выйти')
        elif action == 'speed':
            draw(x, y, w, h, ac, 'Скорость: {}'.format(speed))
        elif action == 'durability':
            draw(x, y, w, h, ac, 'Прочность блоков: {}'.format(durability))
        elif action == 'amount':
            draw(x, y, w, h, ac, 'Количество линий: {}'.format(amount))
        elif action == 'pause':
            draw(x, y, w, h, ac, 'Пауза')
        elif action == 'menu':
            draw(x, y, w, h, ac, 'Меню')
        elif action == 'theme':
            draw(x, y, w, h, ac, 'Тема: {}'.format(theme))
    else:
        if action == 'start':
            draw(x, y, w, h, ic, 'Начать')
        elif action == 'exit':
            draw(x, y, w, h, ic, 'Выйти')
        elif action == 'speed':
            draw(x, y, w, h, ic, 'Скорость: {}'.format(speed))
        elif action == 'durability':
            draw(x, y, w, h, ic, 'Прочность блоков: {}'.format(durability))
        elif action == 'amount':
            draw(x, y, w, h, ic, 'Количество линий: {}'.format(amount))
        elif action == 'pause':
            draw(x, y, w, h, ic, 'Пауза')
        elif action == 'menu':
            draw(x, y, w, h, ic, 'Меню')
        elif action == 'theme':
            draw(x, y, w, h, ic, 'Тема: {}'.format(theme))


all_sprites = pygame.sprite.Group()


class Gun(pygame.sprite.Sprite):
    if theme == 'Цветочная':
        image = load_image("data/images/flower_theme/gun.png")

    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y
        super().__init__(all_sprites)
        self.image = pygame.transform.scale(Ball.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, dir):
        running = True
        while running:
            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if key[pygame.K_DOWN]:
                    self.x -= 10
                    self.rect = self.rect.move(self.x, self.y)
                elif key[pygame.K_UP]:
                    self.y -= 10
                    self.rect = self.rect.move(self.x, self.y)

    def shoot(self):
        pass


class Block(pygame.sprite.Sprite):
    def move(self):
        pass

    def line(self):
        pass

    def check(self):
        pass


class Ball(pygame.sprite.Sprite):
    if theme == 'Цветочная':
        image = load_image("data/images/flower_theme/ball.png")

    def __init__(self, size, x, y):
        super().__init__(all_sprites)
        self.image = pygame.transform.scale(Ball.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def contact(self):
        global vertical_borders
        if pygame.sprite.spritecollideany(self, vertical_borders):
            pass

    def move(self):
        pass

    def remove(self):
        pass


class Border(pygame.sprite.Sprite):
    # строго вертикальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)


def menu_window():
    global theme_list, speed_list, durability_list, amount_list, theme_num, speed_num, durability_num, \
        amount_num, theme, speed, durability, amount
    speed = speed_list[speed_num]
    durability = durability_list[durability_num]
    amount = amount_list[amount_num]
    running = True
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (102, 230, 255)
    screen.fill(BLACK)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 850 <= event.pos[0] <= 1000 and 550 <= event.pos[1] <= 600:
                    set_parameters(theme, speed, durability, amount)
                    game_window()
                if 0 <= event.pos[0] <= 150 and 550 <= event.pos[1] <= 600:
                    pygame.quit()
                if 325 <= event.pos[0] <= 675 and 175 <= event.pos[1] <= 250:
                    if theme_num == 0:
                        theme_num = 0
                    else:
                        theme_num += 1
                    theme = theme_list[theme_num]
                    theme = 'Цветочная'
                    screen.fill(BLACK)
                    draw(325, 175, 350, 75, WHITE, 'Тема: {}'.format(theme))
                if 325 <= event.pos[0] <= 675 and 275 <= event.pos[1] <= 350:
                    if speed_num == 3:
                        speed_num = 0
                    else:
                        speed_num += 1
                    speed = speed_list[speed_num]
                    screen.fill(BLACK)
                    draw(325, 275, 350, 75, WHITE, 'Скорость: {}'.format(speed))
                if 325 <= event.pos[0] <= 675 and 375 <= event.pos[1] <= 450:
                    if durability_num == 3:
                        durability_num = 0
                    else:
                        durability_num += 1
                    durability = durability_list[durability_num]
                    screen.fill(BLACK)
                    draw(325, 375, 350, 75, WHITE, 'Прочность блоков: {}'.format(durability))
                if 325 <= event.pos[0] <= 675 and 475 <= event.pos[1] <= 550:
                    if amount_num == 2:
                        amount_num = 0
                    else:
                        amount_num += 1
                    amount = amount_list[amount_num]
                    screen.fill(BLACK)
                    draw(325, 475, 350, 75, WHITE, 'Количество линий: {}'.format(amount))
        draw(850, 550, 150, 50, WHITE, 'Начать')
        draw(0, 550, 150, 50, WHITE, 'Выйти')
        draw(325, 175, 350, 75, WHITE, 'Тема: {}'.format(theme))
        draw(325, 275, 350, 75, WHITE, 'Скорость: {}'.format(speed))
        draw(325, 375, 350, 75, WHITE, 'Прочность блоков: {}'.format(durability))
        draw(325, 475, 350, 75, WHITE, 'Количество линий: {}'.format(amount))
        draw(525, 50, 350, 75, WHITE, 'Рекорд: {}'.format(best_score))
        draw(125, 50, 350, 75, WHITE, 'Результат: {}'.format(last_score))

        button(850, 550, 150, 50, WHITE, BLUE, action='start')
        button(0, 550, 150, 50, WHITE, BLUE, action='exit')
        button(325, 175, 350, 75, WHITE, BLUE, action='theme')
        button(325, 275, 350, 75, WHITE, BLUE, action='speed')
        button(325, 375, 350, 75, WHITE, BLUE, action='durability')
        button(325, 475, 350, 75, WHITE, BLUE, action='amount')
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()


def game_window():
    running = True
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    screen.fill((225, 225, 0))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 850 <= event.pos[0] <= 1000 and 550 <= event.pos[1] <= 600:
                    menu_window()
                if 0 <= event.pos[0] <= 150 and 550 <= event.pos[1] <= 600:
                    pygame.quit()
                if 425 <= event.pos[0] <= 475 and 560 <= event.pos[1] <= 600:
                    pass
        pygame.draw.line(screen, BLACK, [878, 0], [878, 550], 4)
        for i in range(1, amount + 1):
            y = i * 550 / amount
            pygame.draw.line(screen, BLACK, [0, y], [1000, y], 1)
        draw(850, 560, 150, 40, BLACK, 'Меню')
        draw(0, 560, 150, 40, BLACK, 'Выйти')
        draw(425, 560, 150, 40, BLACK, 'Пауза')
        button(850, 560, 150, 40, BLACK, BLUE, action='menu')
        button(0, 560, 150, 40, BLACK, BLUE, action='exit')
        button(425, 560, 150, 40, BLACK, BLUE, action='pause')

        all_sprites.draw(screen)
        pygame.display.flip()
        if amount == 5:
            Gun(110, 890, 0)
    pygame.quit()
    Border(874, 0, 874, 600)


def end_winodw():
    pass


if __name__ == '__main__':
    # pygame.mouse.set_visible(False)

    pygame.init()
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PyGame")

    fps = 40
    best_score = 15
    last_score = 10

    menu_window()

    pygame.quit()
