import pygame

CUBE_SIZE = 90
CUBE_COLOR = (132, 122, 97)
SELECTED_CUBE_COLOR = (132, 122, 97, 128)
SELECTION_BORDER_COLOR = (255, 128, 0, 128)

cube_count = 0


class Cube(pygame.sprite.Sprite):
    def __init__(self, x, y, selectable):
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
        self._selectable = selectable
        self._hovered = False

    def select(self):
        if self._selectable:
            self._selected = True
        return self._selected

    def unselect(self):
        self._selected = False

    def mouseover(self):
        self._hovered = True

    def mouseout(self):
        self._hovered = False

    def update(self):
        self.image.fill((255, 255, 255, 0))

        if self._selectable and self._hovered:
            pygame.draw.rect(self.image, SELECTION_BORDER_COLOR, [0, 0, CUBE_SIZE, CUBE_SIZE], 10, 10)

        if self._selected:
            pygame.draw.rect(self.image, SELECTED_CUBE_COLOR, [3, 3, CUBE_SIZE - 6, CUBE_SIZE - 6], 0, 10)
        else:
            pygame.draw.rect(self.image, CUBE_COLOR, [3, 3, CUBE_SIZE - 6, CUBE_SIZE - 6], 0, 10)
