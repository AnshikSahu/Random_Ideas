import pygame
import sys
import time

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Draggable Ball with Pause Button")

class Ball:
    def __init__(self, x, y, mass, radius):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.w = 0
        self.a = 0
        self.mass = mass
        self.radius = radius
        self.dragging = False

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)

    def update(self, dt):
        if not self.dragging:
            self.vx += self.ax * dt
            self.vy += self.ay * dt
            self.x += self.vx * dt
            self.y += self.vy * dt
            self.w += self.a * dt
        print(self.x, self.y)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_mouse_on_ball(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.vx = (event.pos[0] - self.x) / 0.01
                self.vy = (event.pos[1] - self.y) / 0.01
                self.x, self.y = event.pos

    def is_mouse_on_ball(self, pos):
        mouse_x, mouse_y = pos
        return (mouse_x - self.x)**2 + (mouse_y - self.y)**2 <= self.radius**2

class Button:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (200, 200, 200)

    def draw_pause(self):
        # Draw two vertical bars for the pause symbol
        bar_width = self.rect.width // 4
        bar_height = self.rect.height * 2 // 3
        bar_spacing = self.rect.width // 3
        pygame.draw.rect(screen, self.color, (self.rect.x + bar_spacing // 2, self.rect.y + (self.rect.height - bar_height) // 2, bar_width, bar_height))
        pygame.draw.rect(screen, self.color, (self.rect.x + bar_spacing // 2 + bar_spacing, self.rect.y + (self.rect.height - bar_height) // 2, bar_width, bar_height))

    def draw_play(self):
        # Draw a right-pointing triangle for the play symbol
        points = [
            (self.rect.x + self.rect.width // 4, self.rect.y + self.rect.height // 4),
            (self.rect.x + self.rect.width // 4, self.rect.y + 3 * self.rect.height // 4),
            (self.rect.x + 3 * self.rect.width // 4, self.rect.y + self.rect.height // 2)
        ]
        pygame.draw.polygon(screen, self.color, points)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

ball = Ball(100, 100, 1, 10)
pause_button = Button(10, 10, 50, 50)
paused = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pause_button.is_clicked(event.pos):
                paused = not paused
        ball.handle_event(event)

    screen.fill((0, 0, 0))
    if paused:
        pause_button.draw_play()
    else:
        pause_button.draw_pause()
    ball.draw()
    if not paused:
        ball.update(0.01)
    pygame.display.flip()
    time.sleep(0.01)
