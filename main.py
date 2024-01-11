from FlashCards import Flashcards
import pygame
import sys
from tkinter.simpledialog import askstring
import random

WIDTH = 900
HEIGHT = 900

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
title = "FlashCards X"
pygame.display.set_caption(title)
clock = pygame.time.Clock()
FPS = 60

flash = Flashcards()

pygame.font.init()
ARIAL = pygame.font.SysFont("arialblack", 75)
smallerARIAL = pygame.font.SysFont("arialblack", 70)
smallestARIAL = pygame.font.SysFont("arialblack", 45)

TITLE = ARIAL.render("FlashCards X", True, (255, 255, 255))
ADD = smallestARIAL.render("(Press 'a' to add a new Flash Card)", True, (255, 255, 255))


new = False

running = True

last_value = list(flash.flashcards.values())[-1]

flashcardsRect = pygame.Rect(WIDTH - 760, 140, 600, 600)

displayOriginal = True

index = 0
cardsIndex = 0

length = 0

while running:
    length = len(flash.flashcards.keys())

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                displayOriginal = True
                cardsIndex = random.randint(cardsIndex + 1, length + 1)
                if cardsIndex > length - 1:
                    cardsIndex = 0
            elif event.key == pygame.K_LEFT:
                displayOriginal = True
                cardsIndex -= 1
                if cardsIndex < length - 1:
                    cardsIndex = 0
            elif event.key == pygame.K_a:
                original = askstring("Add Flash Card", "Original:")
                translation = askstring("Add Flash Card", "Translation:")

                with open(flash.flashfile, "a") as f:
                    f.write(f"{original}|{translation}\n")

                flash.flashcards[original] = translation
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (
                    WIDTH - 760 <= mouse_x <= WIDTH - 760 + 600
                    and 140 <= mouse_y <= 140 + 600
                ):
                    displayOriginal = False
                    index += 1

    screen.fill((12, 42, 90))
    screen.blit(TITLE, (WIDTH / 2 - 280, 0))
    screen.blit(ADD, (WIDTH / 2 - 420, HEIGHT - 90))
    pygame.draw.rect(screen, (255, 255, 255), flashcardsRect, border_radius=20)

    if index % 2 == 0:
        displayOriginal = True
    else:
        displayOriginal = False

    for i in range(length):
        if displayOriginal:
            TEXT = smallerARIAL.render(list(flash.flashcards.keys())[cardsIndex], True, (0, 0, 0))
            text_rect = TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            screen.blit(TEXT, text_rect)
        else:
            TEXT = smallerARIAL.render(list(flash.flashcards.values())[cardsIndex], True, (0, 0, 0))
            text_rect = TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            screen.blit(TEXT, text_rect)

    pygame.display.update()