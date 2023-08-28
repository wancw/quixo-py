import sys
import pygame

from constants import BACKGROUND_COLOR, BOARD_COLOR, PLAY_AREA_SIZE, PLAY_AREA_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT, \
    BOARD_RADIUS, CUBE_SIZE, FPS
from cube import Cube


def main():
    pygame.init()

    main_clock = pygame.time.Clock()

    window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
    pygame.display.set_caption('Quixo')

    # Background
    background = pygame.Surface(window_surface.get_size())
    background.fill(BACKGROUND_COLOR)
    pygame.draw.circle(background, BOARD_COLOR, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), BOARD_RADIUS)

    play_area_left = (SCREEN_WIDTH - PLAY_AREA_SIZE) / 2
    play_area_top = (SCREEN_HEIGHT - PLAY_AREA_SIZE) / 2

    play_area = pygame.Rect(play_area_left, play_area_top, PLAY_AREA_SIZE, PLAY_AREA_SIZE)
    pygame.draw.rect(background, PLAY_AREA_COLOR, play_area, 0, 10)

    # Cubes
    all_cubes: pygame.sprite.Group[Cube] = pygame.sprite.Group()
    for r in range(5):
        for c in range(5):
            cube = Cube(play_area_left + CUBE_SIZE * r, play_area_top + CUBE_SIZE * c)
            all_cubes.add(cube)
    select_cube = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if select_cube is not None:
                    select_cube.unselect()
                for cube in all_cubes.sprites():
                    if cube.rect.collidepoint(event.pos):
                        if cube == select_cube:
                            select_cube = None
                        else:
                            cube.select()
                            select_cube = cube
                        break

        all_cubes.update()

        window_surface.blit(background, (0, 0))
        for cube in all_cubes.sprites():
            window_surface.blit(cube.image, cube.rect)

        pygame.display.flip()

        main_clock.tick(FPS)


if __name__ == '__main__':
    main()
