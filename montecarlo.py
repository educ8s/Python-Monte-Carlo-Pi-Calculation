from tkinter import font
from turtle import circle
import pygame
import random
from sys import exit


def calculate_pi(n,screen):
    inside = 0
    for i in range(n):
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        if x * x + y * y <= 300*300:
            inside += 1
            circle_surface= pygame.Surface((2,2))
            circle_surface.fill("red")
            screen.blit(circle_surface, (x+400, y+500))
            pygame.display.update()
            print(f"{x+400}, {y+500}")
        else:
            circle_surface= pygame.Surface((2,2))
            circle_surface.fill("green")
            screen.blit(circle_surface, (x+400, y+500))
            pygame.display.update()
            print(f"{x+400}, {y+500}")
    return 4 * inside / n

pygame.init()
screen = pygame.display.set_mode((800, 900))
pygame.display.set_caption("Monte Carlo Pi Estimation")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)


test_surface = pygame.Surface((100, 200))
test_surface.fill("red")
text_surface = test_font.render("Monte Carlo Pi Estimation", True, "white")
pi_surface = test_font.render("Pi:", True, "white")
screen.blit(text_surface, (200, 20))
screen.blit(pi_surface, (200, 80))
pygame.display.update()
pi = calculate_pi(50000,screen)
print(pi)
pi_surface = test_font.render(f"Pi: {pi}", True, "white")
screen.blit(pi_surface, (200, 80))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

