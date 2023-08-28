import pygame

from constants import CUBE_SIZE, CUBE_COLOR, SELECTED_CUBE_COLOR

cube_count = 0


class Cube(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([CUBE_SIZE, CUBE_SIZE], pygame.SRCALPHA)
        self.image.fill((255, 255, 255, 0))

        pygame.draw.rect(self.image, CUBE_COLOR, [3, 3, CUBE_SIZE - 6, CUBE_SIZE - 6], 0, 10)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.width = CUBE_SIZE
        self.height = CUBE_SIZE

        global cube_count
        cube_count += 1
        self._id = cube_count

        self._selected = False

    def select(self):
        self._selected = True

    def unselect(self):
        self._selected = False

    def update(self):
        super().update()
        self.image.fill((255, 255, 255, 0))
        if self._selected:
            pygame.draw.rect(self.image, SELECTED_CUBE_COLOR, [3, 3, CUBE_SIZE - 6, CUBE_SIZE - 6], 0, 10)
        else:
            pygame.draw.rect(self.image, CUBE_COLOR, [3, 3, CUBE_SIZE - 6, CUBE_SIZE - 6], 0, 10)
