# Minimal sprite test
#
# * Clear the whole screen
# * Blit the sprite to screen
# * Flip the display
#
# 450 FPS

import playground
import pygame


sprite = pygame.sprite.Sprite()
sprite.image = pygame.Surface((100, 100))
sprite.image.fill((128, 128, 128))
sprite.rect = sprite.image.get_rect()


def update(screen: pygame.Surface):
    screen.fill((0, 0, 0))
    screen.blit(sprite.image, sprite.rect)
    pygame.display.flip()


def event_handler(event: pygame.event.Event):
    if event.type == pygame.MOUSEMOTION:
        sprite.rect.move_ip(event.rel)


playground.loop(update, event_handler)