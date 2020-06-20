# Only redraw the sprite if it has changed
#
# 3333...10000 FPS (depending on events)

import playground
import pygame


spriteA = pygame.sprite.Sprite()
spriteA.image = pygame.Surface((100, 100))
spriteA.image.fill((128, 128, 128))
spriteA.rect = spriteA.image.get_rect()
spriteA.previous_rect = spriteA.rect.copy()
spriteA.has_changed = True

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
spriteB.has_changed = True

all_sprites = pygame.sprite.Group()
all_sprites.add(spriteA, spriteB)


def draw(screen, sprite):
    if not sprite.has_changed:
        return
    sprite.has_changed = False

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
    draw(screen, spriteA)
    draw(screen, spriteB)


def event_handler(event: pygame.event.Event):
    if event.type == pygame.MOUSEMOTION:
        spriteA.rect.move_ip(event.rel)
        spriteA.has_changed = True


playground.loop(update, event_handler)
