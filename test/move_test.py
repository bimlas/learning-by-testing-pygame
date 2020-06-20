import unittest
import pygame


class MoveTestCase(unittest.TestCase):

    def test_rect(self):
        rect_a = pygame.Rect(0, 0, 10, 10)

        self.assertTrue(rect_a.collidepoint(5, 5))

        rect_a.move_ip(15, 15)

        self.assertFalse(rect_a.collidepoint(5, 5))


if __name__ == '__main__':
    unittest.main()
