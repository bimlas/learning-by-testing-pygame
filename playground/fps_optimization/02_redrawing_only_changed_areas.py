import playground
import pygame


sprite = pygame.sprite.Sprite()
sprite.image = pygame.Surface((100, 100))
sprite.image.fill((128, 128, 128))
sprite.rect = sprite.image.get_rect()
sprite.previous_rect = sprite.image.get_rect()

fixed_element = pygame.sprite.Sprite()
fixed_element.image = pygame.Surface((300, 300))
fixed_element.image.fill((0, 128, 128))
fixed_element.rect = fixed_element.image.get_rect()
fixed_element.rect.move_ip(200, 200)
fixed_element.is_drawn = False


def update(screen: pygame.Surface):
    if not fixed_element.is_drawn:
        screen.blit(fixed_element.image, fixed_element.rect)
        pygame.display.update(fixed_element.rect)
        fixed_element.is_drawn = True

    screen.fill((0, 0, 0), sprite.previous_rect)
    screen.blit(sprite.image, sprite.rect)

    pygame.display.update([sprite.previous_rect, sprite.rect])
    # Save the previous position right after drawing at there.
    sprite.previous_rect = sprite.rect.copy()


def event_handler(event: pygame.event.Event):
    if event.type == pygame.MOUSEMOTION:
        # Do not store the previous position here, because if the mousemoution
        # event occurs more than once between two drawings, it will not save
        # the last drawn rect, but the position that was in the penultimate
        # mousemotion event.
        #
        # sprite.previous_rect = sprite.rect.copy()
        sprite.rect.move_ip(event.rel)


playground.loop(update, event_handler)
