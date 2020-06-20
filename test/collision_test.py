import unittest
import pygame
from typing import Tuple


class TransparentSprite(pygame.sprite.Sprite):

    def __init__(self, center: Tuple[int, int], size: Tuple[int, int]):
        super().__init__()
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(center=center)
        self.mask = pygame.mask.from_surface(self.image)
        self.image.fill((255, 255, 255, 0))

    def makeItNonTransparent(self):
        self.image.fill((255, 255, 255, 255))
        return self


class CollisionTestCase(unittest.TestCase):

    def test_rect_with_point(self):
        rect_a = pygame.Rect(0, 0, 10, 10)

        self.assertTrue(rect_a.collidepoint(5, 5))
        self.assertFalse(rect_a.collidepoint(15, 15))

    def test_rects(self):
        rect_a = pygame.Rect(0, 0, 10, 10)
        rect_b = pygame.Rect(5, 5, 15, 15)
        rect_c = pygame.Rect(12, 12, 22, 22)

        self.assertTrue(rect_a.colliderect(rect_b))
        self.assertTrue(rect_b.colliderect(rect_c))
        self.assertFalse(rect_a.colliderect(rect_c))

    def test_surfaces(self):
        surface_a = pygame.Surface((10, 10))
        surface_b = pygame.Surface((10, 10))

        self.assertRaises(AttributeError, lambda: surface_a.colliderect(surface_b))

        rect_a = surface_a.get_rect()
        rect_b = surface_b.get_rect()

        self.assertTrue(rect_a.colliderect(rect_b))

    def test_sprite_rects(self):

        sprite_a = TransparentSprite((10, 10), (15, 15))
        sprite_b = TransparentSprite((20, 20), (15, 15))
        sprite_c = TransparentSprite((30, 30), (15, 15))

        self.assertTrue(pygame.sprite.collide_rect(sprite_a, sprite_b))
        self.assertFalse(pygame.sprite.collide_rect(sprite_a, sprite_c))

    def test_sprite_with_groups(self):

        sprite_a = TransparentSprite((10, 10), (15, 15))
        sprite_b = TransparentSprite((20, 20), (15, 15))
        sprite_c = TransparentSprite((30, 30), (15, 15))

        group = pygame.sprite.Group()

        sprite_a.add(group)
        self.assertEqual([sprite_a], pygame.sprite.spritecollide(sprite_a, group, dokill=False), 'A sprite mindig utkozik a sajat csoportjaval')

        group = pygame.sprite.Group()

        sprite_c.add(group)
        self.assertFalse(pygame.sprite.spritecollide(sprite_a, group, dokill=False))

        sprite_b.add(group)
        self.assertEqual([sprite_b], pygame.sprite.spritecollide(sprite_a, group, dokill=False))

        group = pygame.sprite.Group()

        sprite_a.add(group)
        sprite_c.add(group)
        self.assertEqual([sprite_a, sprite_c], pygame.sprite.spritecollide(sprite_b, group, dokill=False))

    # TODO: Skipped
    def xtest_sprite_masks(self):
        sprite_a = TransparentSprite((10, 10), (15, 15))
        sprite_b = TransparentSprite((20, 20), (15, 15))
        sprite_c = TransparentSprite((30, 30), (15, 15))

        self.assertFalse(pygame.sprite.collide_mask(sprite_a, sprite_b))
        self.assertFalse(pygame.sprite.collide_mask(sprite_a, sprite_c))

        sprite_a.makeItNonTransparent().update()
        sprite_b.makeItNonTransparent().update()
        sprite_c.makeItNonTransparent().update()

        self.assertTrue(pygame.sprite.collide_mask(sprite_a, sprite_b))
        self.assertFalse(pygame.sprite.collide_mask(sprite_a, sprite_c))


if __name__ == '__main__':
    unittest.main()
