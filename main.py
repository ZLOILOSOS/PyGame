import pygame
import sys
import os
import random
from random import randint

with open('data/last_score.txt', encoding='utf8') as f1:
    last_score_txt = f1.readlines()

with open('data/best_score.txt', encoding='utf8') as f2:
    best_score_txt = f2.readlines()

best_score = best_score_txt[0]
last_score = last_score_txt[0]
f1.close()
f2.close()
theme_list = ['Тёмная', 'Светлая', 'Цветочная']
theme_num = 0
theme = theme_list[theme_num]
speed_list = [15, 30, 45, 60]
durability_list = [1, 2, 3, 4]
amount_list = [5, 8, 10]
speed_num = 0
durability_num = 0
amount_num = 0
speed = speed_list[speed_num]
durability = durability_list[durability_num]
amount = amount_list[amount_num]
hit = 0
stat = ''
end = 0
score = 0
all_sprites = pygame.sprite.Group()
group_gun = pygame.sprite.Group()
group_blocks = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def draw(x, y, w, h, clr, txt):
    font = pygame.font.SysFont("consolas", 30)
    text = font.render(txt, False, clr)
    screen.blit(text, (x + 20, y + 20))
    if 'Рекорд' not in txt and 'Результат' not in txt:
        pygame.draw.rect(screen, clr, (x, y, w + 15, h), 1)


def clear_sprites():  # удаляет все спрайты с экрана
    global all_sprites, group_gun, group_blocks, stat, end, hit
    hit = 0
    stat = ''
    end = 0
    all_sprites = pygame.sprite.Group()  # группа для шаров
    group_gun = pygame.sprite.Group()  # группа для пушки
    group_blocks = pygame.sprite.Group()  # группа для блоков


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


class Ball(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        if theme == 'Цветочная':
            image = load_image("data/images/flower_theme/ball.png", -1)
        if theme == 'Тёмная':
            image = load_image("data/images/dark_theme/ball.png", -1)
        if theme == 'Светлая':
            image = load_image("data/images/light_theme/ball.png", -1)
        self.size = size
        self.x = x
        self.y = y
        super().__init__(all_sprites)
        self.image = pygame.transform.scale(image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)
        self.vx = -10

    def move(self, speed):
        if self.rect.x - self.vx > 1:
            self.rect.x += self.vx
        if self.rect.x < 0:
            self.kill()

    def update(self):
        global end
        if self.rect.x >= 0:
            self.rect.x += self.vx
            if self.rect.x < 1:
                self.kill()
            clock.tick(fps)
        else:
            self.kill()
        if end == 1:
            self.kill()


class Gun(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        if theme == 'Цветочная':
            image = load_image("data/images/flower_theme/gun.png", -1)
        if theme == 'Тёмная':
            image = load_image("data/images/dark_theme/gun.png", -1)
        if theme == 'Светлая':
            image = load_image("data/images/light_theme/gun.png", -1)
        super().__init__(group_gun)
        self.size = size
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = (x, y)

    def move(self, k):
        if amount == 5:
            per = 110
        if amount == 8:
            per = 69
        if amount == 10:
            per = 55
        if k == 1:
            self.rect.y += per
        if k == 0:
            self.rect.y -= per

    def update(self):
        pass

    def shoot(self, speed, perr, gun_check):
        self.perr = perr
        self.gun_check = gun_check
        ball = Ball(self.size // 2, self.x + self.perr // 4, self.y + (self.perr * self.gun_check) + self.perr // 4)
        ball.move(speed)


class Block(pygame.sprite.Sprite):
    def __init__(self, size, perr):
        global hit, durability, amount
        self.bl = random.randint(0, 3)
        image = load_image("data/images/flower_theme/blocks/block_{}_{}.png".format(str(0), str(self.bl)))
        self.amount = amount
        self.durability = durability
        self.perr = perr
        self.size = size * 0.8
        self.x = 0
        self.y = self.perr * randint(0, self.amount - 1)
        super().__init__(group_blocks)
        self.image = pygame.transform.scale(image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x + self.size * 0.1, self.y + self.size * 0.1)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        global hit, durability, all_sprites, score, speed
        self.vx = 7
        if self.rect.x + self.vx < 1007 - self.perr - self.size:
            self.rect.x += self.vx
        else:
            self.kill()
            clear_sprites()
            end_winodw()
        if pygame.sprite.spritecollide(self, all_sprites, True):
            hit += 1
            image = load_image("data/images/flower_theme/blocks/block_{}_{}.png".format(str(hit), str(self.bl)))
            self.image = pygame.transform.scale(image, (self.size, self.size))
            if hit == durability:
                score += 1
                self.kill()
                hit = 0


def menu_window():
    global theme_list, speed_list, durability_list, amount_list, theme_num, speed_num, durability_num, \
        amount_num, theme, speed, durability, amount, stat, best_score, last_score
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
            image1 = load_image("data/images/flower_theme/background.png")
            image = pygame.transform.scale(image1, (1000, 600))
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
    global end, speed, bal, block, score, last_score, best_score
    running = True
    if amount == 5:
        s, x1, y1 = 110, 880, 0
        perr = 110
    elif amount == 8:
        s, x1, y1 = 68, 922, 0
        perr = 69
    elif amount == 10:
        s, x1, y1 = 55, 935, 0
        perr = 55
    gun = Gun(s, x1, y1)
    gun_check = 0
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (102, 230, 255)
    GREEN = (0, 255, 0)
    PINK = (230, 50, 230)
    reload = pygame.time.get_ticks()
    reloading = 1
    reload1 = pygame.time.get_ticks()
    reloading1 = 1
    color1 = WHITE
    color2 = BLUE
    color3 = WHITE
    color4 = WHITE
    screen.fill(BLACK)
    pygame.display.flip()
    am = 60 / speed * 2
    while running:
        if (pygame.time.get_ticks() - reload1) // (20000 / speed) and reloading1 <= 1:
            reload1 = pygame.time.get_ticks()
            reloading1 += 1
        if (pygame.time.get_ticks() - reload) // (60000 / speed) and reloading <= 1:
            reload = pygame.time.get_ticks()
            reloading += 1
        if reloading:
            block = Block(s, perr)
            reloading -= 1
        key = pygame.key.get_pressed()
        if theme == 'Цветочная':
            image1 = load_image("data/images/flower_theme/background.png")
            image = pygame.transform.scale(image1, (1000, 600))
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if gun_check < amount - 1:
                        gun_check += 1
                        gun.move(1)
                elif event.key == pygame.K_UP:
                    if gun_check > 0:
                        gun_check -= 1
                        gun.move(0)
                elif event.key == pygame.K_SPACE:
                    if reloading1 > 0:
                        gun.shoot(speed, perr, gun_check)
                        reloading1 -= 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 850 <= event.pos[0] <= 1000 and 550 <= event.pos[1] <= 600:
                    clear_sprites()
                    menu_window()
                if 0 <= event.pos[0] <= 150 and 550 <= event.pos[1] <= 600:
                    pygame.quit()
                if 425 <= event.pos[0] <= 575 and 550 <= event.pos[1] <= 600:
                    clear_sprites()
                    score = 0
                    game_window()
        if amount == 5:
            pygame.draw.line(screen, color4, [878, 0], [878, 550], 4)
        elif amount == 8:
            pygame.draw.line(screen, color4, [920, 0], [920, 550], 4)
        elif amount == 10:
            pygame.draw.line(screen, color4, [933, 0], [933, 550], 4)
        for i in range(1, amount + 1):
            y = i * 550 / amount
            pygame.draw.line(screen, color3, [0, y], [1000, y], 1)
        draw(575, 550, 150, 50, color1, 'Рекорд: {}'.format(best_score))
        draw(150, 550, 150, 50, color1, 'Результат: {}'.format(score))

        button(850, 550, 150, 50, color1, color2, action='menu')
        button(0, 550, 150, 50, color1, color2, action='exit')
        button(425, 550, 150, 50, color1, color2, action='retry')
        clock.tick(60)
        group_gun.draw(screen)
        all_sprites.draw(screen)
        group_blocks.draw(screen)
        group_gun.update()
        all_sprites.update()
        group_blocks.update()
        pygame.display.flip()
    pygame.quit()


def end_winodw():
    global score, last_score, best_score
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
            image1 = load_image("data/images/flower_theme/background.png")
            image = pygame.transform.scale(image1, (1000, 600))
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
                if 850 <= event.pos[0] <= 1000 and 550 <= event.pos[1] <= 600:
                    menu_window()
                if 0 <= event.pos[0] <= 150 and 550 <= event.pos[1] <= 600:
                    pygame.quit()
                if 425 <= event.pos[0] <= 575 and 550 <= event.pos[1] <= 600:
                    game_window()
        if score == int(best_score):
            mes1 = 'Ты набрал(а) '
            mes2 = ' очков'
            last_score = score
            a = 600
            b = 225
        elif score > int(best_score):
            best_score = score
            last_score = score
            mes1 = 'Ого, целых '
            mes2 = ' очков, молодец'
            a = 500
            b = 250
        elif score < int(best_score):
            last_score = score
            mes1 = 'Всего '
            mes2 = ' очков, ничего в следуюший раз будет лучше'
            a = 850
            b = 75
        best = open("data/best_score.txt", 'w')
        last = open("data/last_score.txt", 'w')
        best.write(str(best_score))
        last.write(str(last_score))
        draw(400, 50, 400, 75, color1, 'Ваш Рекорд: {}'.format(best_score))
        draw(b, 150, a, 75, color1, mes1 + str(score) + mes2)
        button(850, 550, 150, 50, color1, color2, action='menu')
        button(0, 550, 150, 50, color1, color2, action='exit')
        button(425, 550, 150, 50, color1, color2, action='retry')
        pygame.display.flip()
        best.close()
        last.close()
    score = 0
    pygame.quit()


if __name__ == '__main__':
    # pygame.mouse.set_visible(False)

    pygame.init()
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PyGame")

    v = 100
    fps = 60
    clock = pygame.time.Clock()
    menu_window()
    pygame.quit()
