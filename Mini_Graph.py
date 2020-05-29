import pygame
import math

pygame.init()

win = pygame.display.set_mode((490, 500))
pygame.display.set_caption('Mini Graph')
run = True
x = 0
y = 2
cos = pygame.image.load('Cos.png')
sin = pygame.image.load('Sin.png')
log = pygame.image.load('Log.png')
exp = pygame.image.load('Exp.png')
modsin = pygame.image.load('Modsin.png')
modcos = pygame.image.load('Modcos.png')
modsinminus = pygame.image.load('Modsinminus.png')
modcosminus = pygame.image.load('Modcosminus.png')
smiley = pygame.image.load('Smiley.png')
xsinx = pygame.image.load('Xsinx.png')
low = pygame.image.load('Low.png')
medium = pygame.image.load('Medium.png')
high = pygame.image.load('High.png')


class Size(object):
    pen = 1

    def Low(self):
        self.pen = 2

    def Medium(self):
        self.pen = 5

    def High(self):
        self.pen = 10


size = Size()


def Cos():
    win.fill((0, 0, 0))
    x = 0
    y = 5
    while x < 5.6 * math.pi:
        x_new = x + math.pi / 500
        y_new = -(math.cos(x_new)) + 6
        pygame.draw.line(win, (255, 0, 0), (x * 30, y * 30), (x_new * 30, y_new * 30), size.pen)
        y = -(math.cos(x)) + 6
        x += math.pi / 500
        pygame.display.update()
    win.fill((0, 0, 0))


def Sin():
    win.fill((0, 0, 0))
    x = 0
    y = 6
    while x < 5.6 * math.pi:
        x_new = x + math.pi / 500
        y_new = -(math.sin(x_new)) + 6
        pygame.draw.line(win, (0, 255, 0), (x * 30, y * 30), (x_new * 30, y_new * 30), size.pen)
        y = -(math.sin(x)) + 6
        x += math.pi / 500
        pygame.display.update()
    win.fill((0, 0, 0))


def Log():
    win.fill((0, 0, 0))
    x = 0.1
    y = 8
    while x < 5.6 * math.pi:
        x_new = x + math.pi / 500
        y_new = -(math.log(x_new)) + 6
        pygame.draw.line(win, (0, 255, 255), (x * 30, y * 30), (x_new * 30, y_new * 30), size.pen)
        y = -(math.log(x)) + 6
        x += math.pi / 500
        pygame.display.update()
    win.fill((0, 0, 0))


def Exp():
    win.fill((0, 0, 0))
    x = 0
    y = 9
    while x < math.pi:
        x_new = x + math.pi / 5000
        y_new = -(math.exp(x_new)) + 10
        pygame.draw.line(win, (255, 255, 0), (x * 30, y * 30), (x_new * 30, y_new * 30), size.pen)
        y = -(math.exp(x)) + 10
        x += math.pi / 5000
        pygame.display.update()
    win.fill((0, 0, 0))


def Modsin():
    win.fill((0, 0, 0))
    x = 0
    y = 6
    while x < 5.6 * math.pi:
        x_new = x + math.pi / 500
        y_new = -(abs(math.sin(x_new))) + 6
        pygame.draw.line(win, (255, 0, 255), (x * 30, y * 30), (x_new * 30, y_new * 30), size.pen)
        y = -(abs(math.sin(x))) + 6
        x += math.pi / 500
        pygame.display.update()
    win.fill((0, 0, 0))


def Modcos():
    win.fill((0, 0, 0))
    x = 0
    y = 5
    while x < 5.6 * math.pi:
        x_new = x + math.pi / 500
        y_new = -(abs(math.cos(x_new))) + 6
        pygame.draw.line(win, (0, 100, 255), (x * 30, y * 30), (x_new * 30, y_new * 30), size.pen)
        y = -(abs(math.cos(x))) + 6
        x += math.pi / 500
        pygame.display.update()
    win.fill((0, 0, 0))


def Modsinminus():
    win.fill((0, 0, 0))
    x = 0
    y = 6
    x_ = 0
    y_ = 6
    while x < 5.6 * math.pi and x_ < 5.6 * math.pi:
        x_new = x + math.pi / 500
        y_new = -(abs(math.sin(x_new))) + 6
        pygame.draw.line(win, (180, 100, 0), (x * 30, y * 30), (x_new * 30, y_new * 30), size.pen)
        y = -(abs(math.sin(x))) + 6
        x += math.pi / 500
        x_new_ = x_ + math.pi / 500
        y_new_ = (abs(math.sin(x_new_))) + 6
        pygame.draw.line(win, (180, 100, 0), (x_ * 30, y_ * 30), (x_new_ * 30, y_new_ * 30), size.pen)
        y_ = (abs(math.sin(x))) + 6
        x_ += math.pi / 500
        pygame.display.update()
    win.fill((0, 0, 0))


def Modcosminus():
    win.fill((0, 0, 0))
    x = 0
    y = 5
    x_ = 0
    y_ = 5
    while x < 5.6 * math.pi and x_ < 5.6 * math.pi:
        x_new = x + math.pi / 500
        y_new = -(abs(math.cos(x_new))) + 6
        pygame.draw.line(win, (220, 0, 180), (x * 30, y * 30), (x_new * 30, y_new * 30), size.pen)
        y = -(abs(math.cos(x))) + 6
        x += math.pi / 500
        x_new_ = x_ + math.pi / 500
        y_new_ = (abs(math.cos(x_new_))) + 6
        pygame.draw.line(win, (220, 0, 180), (x_ * 30, y_ * 30), (x_new_ * 30, y_new_ * 30), size.pen)
        y_ = (abs(math.cos(x))) + 6
        x_ += math.pi / 500
        pygame.display.update()
    win.fill((0, 0, 0))


def Smiley():
    win.fill((0, 0, 0))
    x = 0
    y = 5
    x_ = 0
    y_ = 5
    while x < 5.6 * math.pi and x_ < 5.6 * math.pi:
        x_new = x + math.pi / 1500
        y_new = -(abs(math.cos(x_new))) + 6
        pygame.draw.line(win, (200, 150, 60), (x * 30, y * 30), (x_new * 30, y_new * 30), size.pen)
        y = -(abs(math.sin(x))) + 6
        x += math.pi / 1500
        x_new_ = x_ + math.pi / 1500
        y_new_ = (abs(math.cos(x_new_))) + 6
        pygame.draw.line(win, (200, 150, 60), (x_ * 30, y_ * 30), (x_new_ * 30, y_new_ * 30), size.pen)
        y_ = (abs(math.sin(x))) + 6
        x_ += math.pi / 1500
        pygame.display.update()
    win.fill((0, 0, 0))


def Xsinx():
    win.fill((0, 0, 0))
    x = 0
    y = 6
    while x < 5.6 * math.pi:
        x_new = x + math.pi / 500
        y_new = -(x_new * math.sin(x_new)) + 6
        pygame.draw.line(win, (0, 255, 0), (x * 30, y * 30), (x_new * 30, y_new * 30), size.pen)
        y = -(x * math.sin(x)) + 6
        x += math.pi / 500
        pygame.display.update()
    win.fill((0, 0, 0))


while run:
    pygame.time.delay(500)
    win.blit(cos, (0, 460))
    win.blit(sin, (50, 460))
    win.blit(log, (100, 460))
    win.blit(exp, (150, 460))
    win.blit(modsin, (200, 460))
    win.blit(modcos, (250, 460))
    win.blit(modsinminus, (300, 460))
    win.blit(modcosminus, (350, 460))
    win.blit(smiley, (400, 460))
    win.blit(xsinx, (450, 460))
    win.blit(low, (0, 420))
    win.blit(medium, (210, 420))
    win.blit(high, (427, 420))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
        if events.type == pygame.MOUSEBUTTONDOWN:
            if 0 < pygame.mouse.get_pos()[0] < 40 and 460 < pygame.mouse.get_pos()[1] < 500:
                Cos()
            if 50 < pygame.mouse.get_pos()[0] < 90 and 460 < pygame.mouse.get_pos()[1] < 500:
                Sin()
            if 100 < pygame.mouse.get_pos()[0] < 140 and 460 < pygame.mouse.get_pos()[1] < 500:
                Log()
            if 150 < pygame.mouse.get_pos()[0] < 190 and 460 < pygame.mouse.get_pos()[1] < 500:
                Exp()
            if 200 < pygame.mouse.get_pos()[0] < 240 and 460 < pygame.mouse.get_pos()[1] < 500:
                Modsin()
            if 250 < pygame.mouse.get_pos()[0] < 290 and 460 < pygame.mouse.get_pos()[1] < 500:
                Modcos()
            if 300 < pygame.mouse.get_pos()[0] < 340 and 460 < pygame.mouse.get_pos()[1] < 500:
                Modsinminus()
            if 350 < pygame.mouse.get_pos()[0] < 390 and 460 < pygame.mouse.get_pos()[1] < 500:
                Modcosminus()
            if 400 < pygame.mouse.get_pos()[0] < 440 and 460 < pygame.mouse.get_pos()[1] < 500:
                Smiley()
            if 450 < pygame.mouse.get_pos()[0] < 490 and 460 < pygame.mouse.get_pos()[1] < 500:
                Xsinx()
            if 0 < pygame.mouse.get_pos()[0] < 63 and 420 < pygame.mouse.get_pos()[1] < 460:
                size.Low()
            if 210 < pygame.mouse.get_pos()[0] < 273 and 420 < pygame.mouse.get_pos()[1] < 460:
                size.Medium()
            if 427 < pygame.mouse.get_pos()[0] < 490 and 420 < pygame.mouse.get_pos()[1] < 460:
                size.High()
    pygame.display.update()
pygame.quit()
