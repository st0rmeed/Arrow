import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Custom Mouse Cursor")

cursor_image = pygame.image.load(os.path.join('data', 'arrow.png')).convert_alpha()

cursor_rect = cursor_image.get_rect()

pygame.mouse.set_visible(False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    if pygame.mouse.get_focused():
        mouse_pos = pygame.mouse.get_pos()

        cursor_rect.center = mouse_pos

        screen.blit(cursor_image, cursor_rect)

    pygame.display.flip()

pygame.quit()
