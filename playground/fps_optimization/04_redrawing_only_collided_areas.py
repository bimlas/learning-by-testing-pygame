# Redraw only collided areas
#
# * Draw the sprite
# * Save its position
# * Change the sprite position by mousemotion event
# * Fill the previous position with background color
# * Find the sprites that collide with the previous position
# * Redraw the common area of the previous position and the collision
#   sprite from the image of the collision sprite
# * Start again
#
# 3333 FPS

import playground
import pygame


spriteA = pygame.sprite.Sprite()
spriteA.image = pygame.Surface((100, 100))
spriteA.image.fill((128, 128, 128))
spriteA.rect = spriteA.image.get_rect()
spriteA.previous_rect = spriteA.rect.copy()

spriteB = pygame.sprite.Sprite()
spriteB.image = pygame.Surface((300, 300))
spriteB.image.fill((0, 128, 128))
spriteB.image.fill((0, 128, 0), (50, 50, 100, 100))
spriteB.image.fill((0, 128, 0), (150, 150, 100, 100))
spriteB.image.fill((0, 0, 128), (50, 150, 100, 100))
spriteB.image.fill((0, 0, 128), (150, 50, 100, 100))
spriteB.rect = spriteB.image.get_rect()
spriteB.rect.move_ip(200, 200)
spriteB.previous_rect = spriteB.rect.copy()
spriteB.is_drawn = False

all_sprites = pygame.sprite.Group()
all_sprites.add(spriteA, spriteB)


def draw(screen, sprite):
    screen.fill((0, 0, 0), sprite.previous_rect)
    redraw_previous_rect(screen, sprite)
    screen.blit(sprite.image, sprite.rect)
    pygame.display.update([sprite.previous_rect, sprite.rect])
    sprite.previous_rect = sprite.rect.copy()


def redraw_previous_rect(screen: pygame.Surface, sprite: pygame.sprite.Sprite):
    colliding_sprites = pygame.sprite.spritecollide(
        sprite,
        all_sprites,
        dokill=False,
        collided=lambda a, b: a != b and a.previous_rect.colliderect(b.rect)
    )

    for current in colliding_sprites:
        collided_area = sprite.previous_rect.clip(current.rect)
        screen.blit(
            current.image,
            (collided_area.left, collided_area.top),
            area=(
                collided_area.left - current.rect.left,
                collided_area.top - current.rect.top,
                collided_area.width,
                collided_area.height
            )
        )


def update(screen: pygame.Surface):
    if not spriteB.is_drawn:
        draw(screen, spriteB)
        spriteB.is_drawn = True

    draw(screen, spriteA)


def event_handler(event: pygame.event.Event):
    if event.type == pygame.MOUSEMOTION:
        spriteA.rect.move_ip(event.rel)


playground.loop(update, event_handler)
