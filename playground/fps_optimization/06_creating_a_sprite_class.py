# Encapsulate functions to class
#
# 3333...10000 FPS (depending on events)

import playground
import pygame


class Drawable(pygame.sprite.Sprite):
    all_drawables = pygame.sprite.Group()

    def __init__(self, image: pygame.Surface, parent_image: pygame.Surface):
        super().__init__(Drawable.all_drawables)
        self.image = image
        self.rect = self.image.get_rect()
        self.previous_rect = self.rect.copy()
        self.parent_image = parent_image
        self.has_changed = True

    def draw(self):
        if not self.has_changed:
            return
        self.has_changed = False

        self.redraw_previous_rect()
        self.parent_image.blit(self.image, self.rect)
        pygame.display.update([self.previous_rect, self.rect])
        self.previous_rect = self.rect.copy()

    def redraw_previous_rect(self):
        if self.rect == self.previous_rect:
            return

        self.parent_image.fill((0, 0, 0), self.previous_rect)

        colliding_sprites = pygame.sprite.spritecollide(
            self,
            Drawable.all_drawables,
            dokill=False,
            collided=lambda a, b: a != b and a.previous_rect.colliderect(b.rect)
        )

        for current in colliding_sprites:
            collided_area = self.previous_rect.clip(current.rect)
            current.parent_image.blit(
                current.image,
                (collided_area.left, collided_area.top),
                area=(
                    collided_area.left - current.rect.left,
                    collided_area.top - current.rect.top,
                    collided_area.width,
                    collided_area.height
                )
            )

    # TODO: Silly method overloading
    def move(self, x_or_pos, y = None):
        if y is not None:
            self.rect.move_ip(x_or_pos, y)
        else:
            self.rect.move_ip(x_or_pos)
        self.has_changed = True

        return self


sprite = {
    'A': None,
    'B': None,
}


def update(screen: pygame.Surface):
    if sprite['A'] is None:
        sprite['A'] = Drawable(image=pygame.Surface((100, 100)), parent_image=screen)
        sprite['A'].image.fill((128, 128, 128))

        sprite['B'] = Drawable(image=pygame.Surface((300, 300)), parent_image=screen).move(200, 200)
        sprite['B'].image.fill((0, 128, 128))
        sprite['B'].image.fill((0, 128, 0), (50, 50, 100, 100))
        sprite['B'].image.fill((0, 128, 0), (150, 150, 100, 100))
        sprite['B'].image.fill((0, 0, 128), (50, 150, 100, 100))
        sprite['B'].image.fill((0, 0, 128), (150, 50, 100, 100))

    sprite['A'].draw()
    sprite['B'].draw()


def event_handler(event: pygame.event.Event):
    if event.type == pygame.MOUSEMOTION:
        sprite['A'].move(event.rel)


playground.loop(update, event_handler)
