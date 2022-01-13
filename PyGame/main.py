import pygame
import sys
import os

theme_list = ['Тёмная', 'Светлая', 'Цветочная']
theme_num = 0
theme = theme_list[theme_num]
speed_list = [30, 60, 90, 120]
durability_list = [1, 2, 3, 4]
amount_list = [5, 8, 10]
speed_num = 0
durability_num = 0
amount_num = 0
speed = speed_list[speed_num]
durability = durability_list[durability_num]
amount = amount_list[amount_num]
stat = ''
vertical_borders = pygame.sprite.Group()

'''def set_parameters(theme_par, speed_par, durability_par, amount_par):
    if theme_par == '':
        pass
    if speed_par == '':
        pass
    if durability_par == '':
        pass
    if amount_par == '':
        pass'''


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
    font = pygame.font.SysFont("consolas", 30)
    text = font.render(txt, False, clr)
    screen.blit(text, (x + 20, y + 20))
    if 'Рекорд' not in txt and 'Результат' not in txt:
        pygame.draw.rect(screen, clr, (x, y, w + 15, h), 1)


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
        elif action == 'retry':
            draw(x, y, w, h, ac, 'Заново')
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
        elif action == 'retry':
            draw(x, y, w, h, ic, 'Заново')


all_sprites = pygame.sprite.Group()


class Gun(pygame.sprite.Sprite):
    if theme == 'Цветочная':
        image = load_image("data/images/flower_theme/gun.png")
    if theme == 'Тёмная':
        image = load_image("data/images/flower_theme/gun.png")
    if theme == 'Светлая':
        image = load_image("data/images/flower_theme/gun.png")

    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y
        super().__init__(all_sprites)
        self.image1 = Gun.image
        self.image = pygame.transform.scale(self.image1, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)
        '''self.x = x
        self.y = y
        self.mv = 190
        if amount == 5:
            self.mv = 190
        elif amount == 8:
            self.mv = 120
        elif amount == 10:
            self.mv = 95
        Gun.move()'''

    '''def move(self):
        running = True
        while running:
            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if key[pygame.K_DOWN]:
                    self.y -= self.mv
                    self.rect = self.rect.move(self.x, self.y)
                elif key[pygame.K_UP]:
                    self.y += self.mv
                    self.rect = self.rect.move(self.x, self.y)'''

    def dell(self):
        self.x = 1500
        self.rect = self.rect.move(self.x, self.x)

    def shoot(self):
        pass


class Block(pygame.sprite.Sprite):
    if theme == 'Цветочная':
        image = load_image("data/images/flower_theme/gun.png")
    if theme == 'Тёмная':
        image = load_image("data/images/flower_theme/gun.png")
    if theme == 'Светлая':
        image = load_image("data/images/flower_theme/gun.png")

    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y
        super().__init__(all_sprites)
        self.image1 = Gun.image
        self.image = pygame.transform.scale(self.image1, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)
        '''self.x = x
        self.y = y
        self.mv = 190
        if amount == 5:
            self.mv = 190
        elif amount == 8:
            self.mv = 120
        elif amount == 10:
            self.mv = 95
        Gun.move()'''

    '''def move(self):
        running = True
        while running:
            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if key[pygame.K_DOWN]:
                    self.y -= self.mv
                    self.rect = self.rect.move(self.x, self.y)
                elif key[pygame.K_UP]:
                    self.y += self.mv
                    self.rect = self.rect.move(self.x, self.y)'''

    def move(self):
        if stat == 'menu':
            self.kill()

    def line(self):
        pass

    def check(self):
        pass


class Ball(pygame.sprite.Sprite):
    if theme == 'Цветочная':
        image = load_image("data/images/flower_theme/gun.png")
    if theme == 'Тёмная':
        image = load_image("data/images/flower_theme/gun.png")
    if theme == 'Светлая':
        image = load_image("data/images/flower_theme/gun.png")

    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y
        super().__init__(all_sprites)
        self.image1 = Gun.image
        self.image = pygame.transform.scale(self.image1, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)
        '''self.x = x
        self.y = y
        self.mv = 190
        if amount == 5:
            self.mv = 190
        elif amount == 8:
            self.mv = 120
        elif amount == 10:
            self.mv = 95
        Gun.move()'''

    '''def move(self):
        running = True
        while running:
            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if key[pygame.K_DOWN]:
                    self.y -= self.mv
                    self.rect = self.rect.move(self.x, self.y)
                elif key[pygame.K_UP]:
                    self.y += self.mv
                    self.rect = self.rect.move(self.x, self.y)'''

    def contact(self):
        global vertical_borders
        if pygame.sprite.spritecollideany(self, vertical_borders):
            pass

    def move(self):
        if stat == 'menu':
            self.kill()

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
        amount_num, theme, speed, durability, amount, stat
    stat = 'menu'
    speed = speed_list[speed_num]
    durability = durability_list[durability_num]
    amount = amount_list[amount_num]
    running = True
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (102, 230, 255)
    GREEN = (0, 200, 64)
    PINK = (230, 50, 230)
    color1 = WHITE
    color2 = BLUE
    screen.fill(BLACK)
    while running:
        if theme == 'Цветочная':
            image = load_image("data/images/flower_theme/background.png")
            rect = image.get_rect()
            rect.left, rect.top = 0, 0
            screen.blit(image, rect)
            color1 = BLACK
            color2 = GREEN
        elif theme == 'Тёмная':
            screen.fill(BLACK)
            color1 = WHITE
            color2 = BLUE
        elif theme == 'Светлая':
            screen.fill(WHITE)
            color1 = BLACK
            color2 = PINK
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 850 <= event.pos[0] <= 1000 and 535 <= event.pos[1] <= 600:
                    # set_parameters(theme, speed, durability, amount)
                    game_window()
                if 0 <= event.pos[0] <= 150 and 535 <= event.pos[1] <= 600:
                    pygame.quit()
                if 325 <= event.pos[0] <= 695 and 475 <= event.pos[1] <= 550:
                    if theme_num == 2:
                        theme_num = 0
                    else:
                        theme_num += 1
                    theme = theme_list[theme_num]
                if 325 <= event.pos[0] <= 695 and 275 <= event.pos[1] <= 350:
                    if speed_num == 3:
                        speed_num = 0
                    else:
                        speed_num += 1
                    speed = speed_list[speed_num]
                if 325 <= event.pos[0] <= 695 and 375 <= event.pos[1] <= 450:
                    if durability_num == 3:
                        durability_num = 0
                    else:
                        durability_num += 1
                    durability = durability_list[durability_num]
                if 325 <= event.pos[0] <= 695 and 175 <= event.pos[1] <= 250:
                    if amount_num == 2:
                        amount_num = 0
                    else:
                        amount_num += 1
                    amount = amount_list[amount_num]
        draw(525, 50, 350, 75, color1, 'Рекорд: {}'.format(best_score))
        draw(125, 50, 350, 75, color1, 'Результат: {}'.format(last_score))

        button(835, 535, 150, 65, color1, color2, action='start')
        button(0, 535, 150, 65, color1, color2, action='exit')
        button(325, 475, 350, 75, color1, color2, action='theme')
        button(325, 275, 350, 75, color1, color2, action='speed')
        button(325, 375, 350, 75, color1, color2, action='durability')
        button(325, 175, 350, 75, color1, color2, action='amount')
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()


def game_window():
    running = True
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (102, 230, 255)
    GREEN = (0, 255, 0)
    PINK = (230, 50, 230)
    color1 = WHITE
    color2 = BLUE
    color3 = WHITE
    color4 = WHITE
    screen.fill(BLACK)
    pygame.display.flip()
    while running:
        if theme == 'Цветочная':
            image = load_image("data/images/flower_theme/background.png")
            rect = image.get_rect()
            rect.left, rect.top = 0, 0
            screen.blit(image, rect)
            color1 = BLACK
            color2 = GREEN
            color3 = WHITE
            color4 = GREEN
        elif theme == 'Тёмная':
            screen.fill(BLACK)
            color1 = WHITE
            color2 = BLUE
            color3 = WHITE
            color4 = WHITE
        elif theme == 'Светлая':
            screen.fill(WHITE)
            color1 = BLACK
            color2 = PINK
            color3 = BLACK
            color4 = BLACK
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
        if amount == 5:
            pygame.draw.line(screen, color4, [878, 0], [878, 550], 4)
        elif amount == 8:
            pygame.draw.line(screen, color4, [920, 0], [920, 550], 4)
        elif amount == 10:
            pygame.draw.line(screen, color4, [933, 0], [933, 550], 4)
        for i in range(1, amount + 1):
            y = i * 550 / amount
            pygame.draw.line(screen, color3, [0, y], [1000, y], 1)
        button(850, 550, 150, 50, color1, color2, action='menu')
        button(0, 550, 150, 50, color1, color2, action='exit')
        button(425, 550, 150, 50, color1, color2, action='pause')
        if amount == 5:
            Gun(110, 880, 0)
        elif amount == 8:
            Gun(68, 922, 0)
        elif amount == 10:
            Gun(55, 935, 0)

        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()


def end_winodw():
    running = True
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (102, 230, 255)
    GREEN = (0, 255, 0)
    PINK = (230, 50, 230)
    color1 = WHITE
    color2 = BLUE
    color3 = WHITE
    color4 = WHITE
    screen.fill(BLACK)
    pygame.display.flip()
    while running:
        if theme == 'Цветочная':
            image = load_image("data/images/flower_theme/background.png")
            rect = image.get_rect()
            rect.left, rect.top = 0, 0
            screen.blit(image, rect)
            color1 = BLACK
            color2 = GREEN
            color3 = WHITE
            color4 = GREEN
        elif theme == 'Тёмная':
            screen.fill(BLACK)
            color1 = WHITE
            color2 = BLUE
            color3 = WHITE
            color4 = WHITE
        elif theme == 'Светлая':
            screen.fill(WHITE)
            color1 = BLACK
            color2 = PINK
            color3 = BLACK
            color4 = BLACK
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 850 <= event.pos[0] <= 1000 and 550 <= event.pos[1] <= 600:
                    menu_window()
                if 0 <= event.pos[0] <= 150 and 550 <= event.pos[1] <= 600:
                    pygame.quit()
                if 425 <= event.pos[0] <= 475 and 560 <= event.pos[1] <= 600:
                    game_window()
        if last_score > best_score:
            mes1 = ''
            mes2 = ''
        elif last_score + best_score // 5 > best_score:
            mes1 = ''
            mes2 = ''
            draw(525, 50, 350, 75, color1, 'Ваш Рекорд: {}'.format(best_score))
        else:
            mes1 = ''
            mes2 = ''
            draw(525, 50, 350, 75, color1, 'Ваш Рекорд: {}'.format(best_score))
        draw(125, 50, 350, 75, color1, mes1 + str(last_score) + mes2)

        button(850, 550, 150, 50, color1, color2, action='menu')
        button(0, 550, 150, 50, color1, color2, action='exit')
        button(425, 550, 150, 50, color1, color2, action='retry')

        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()


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
