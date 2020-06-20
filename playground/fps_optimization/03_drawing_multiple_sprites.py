import playground
import pygame


spriteA = pygame.sprite.Sprite()
spriteA.image = pygame.Surface((100, 100))
spriteA.image.fill((128, 128, 128))
spriteA.rect = spriteA.image.get_rect()
spriteA.previous_rect = spriteA.image.get_rect()

spriteB = pygame.sprite.Sprite()
spriteB.image = pygame.Surface((300, 300))
spriteB.image.fill((0, 128, 128))
spriteB.rect = spriteB.image.get_rect()
spriteB.rect.move_ip(200, 200)
spriteB.previous_rect = spriteB.image.get_rect()


def draw(screen, sprite):
    screen.fill((0, 0, 0), sprite.previous_rect)
    screen.blit(sprite.image, sprite.rect)
    pygame.display.update([sprite.previous_rect, sprite.rect])
    sprite.previous_rect = sprite.rect.copy()


def update(screen: pygame.Surface):

    draw(screen, spriteA)
    draw(screen, spriteB)


def event_handler(event: pygame.event.Event):
    if event.type == pygame.MOUSEMOTION:
        spriteA.rect.move_ip(event.rel)


playground.loop(update, event_handler)
