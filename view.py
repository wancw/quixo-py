import math
import pygame

from sprite.cube import Cube, CUBE_SIZE

FRAME_PER_SECOND = 60

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
BOARD_RADIUS = 360
PLAY_AREA_SIZE = CUBE_SIZE * 5
BACKGROUND_COLOR = (240, 240, 240)
BOARD_COLOR = (49, 32, 42)
PLAY_AREA_COLOR = (255, 255, 255)

PLAY_AREA_LEFT = (SCREEN_WIDTH - PLAY_AREA_SIZE) / 2
PLAY_AREA_TOP = (SCREEN_HEIGHT - PLAY_AREA_SIZE) / 2


class View:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Quixo')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)

        # Background
        background = pygame.Surface(self.screen.get_size())
        background.fill(BACKGROUND_COLOR)
        pygame.draw.circle(background, BOARD_COLOR, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), BOARD_RADIUS)

        play_area = pygame.Rect(PLAY_AREA_LEFT, PLAY_AREA_TOP, PLAY_AREA_SIZE, PLAY_AREA_SIZE)
        pygame.draw.rect(background, PLAY_AREA_COLOR, play_area, 0, 10)
        self.background = background

        # Cubes
        self.cubes = pygame.sprite.LayeredUpdates()
        for r in range(5):
            for c in range(5):
                cube = Cube(PLAY_AREA_LEFT + CUBE_SIZE * c, PLAY_AREA_TOP + CUBE_SIZE * r,
                            r == 0 or r == 4 or c == 0 or c == 4)
                self.cubes.add(cube)
        self.hovered_cube = None

        self.clock = pygame.time.Clock()

    def update(self):
        self.cubes.update()

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        # for cube in self.cubes.sprites():
        #     self.screen.blit(cube.image, cube.rect)
        self.cubes.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(FRAME_PER_SECOND)

    @staticmethod
    def convert_to_grid(pos):
        x, y = pos
        c = math.floor((x - PLAY_AREA_LEFT) / CUBE_SIZE)
        r = math.floor((y - PLAY_AREA_TOP) / CUBE_SIZE)
        if 0 <= r < 5 and 0 <= c < 5:
            return r, c
        return None

    def on_mouse_over(self, _pos: tuple[int, int]):
        if self.hovered_cube is not None:
            self.hovered_cube.mouseout()
            self.hovered_cube = None

        for cube in self.cubes.sprites():
            if cube.rect.collidepoint(pygame.mouse.get_pos()):
                cube.mouseover()
                self.hovered_cube = cube
                return

    def select_cube(self, cube_id):
        selected_cube = self.cubes.get_sprite(cube_id - 1)
        selected_cube.select()

    def unselect_cube(self, cube_id):
        unselected_cube = self.cubes.get_sprite(cube_id - 1)
        unselected_cube.unselect()
