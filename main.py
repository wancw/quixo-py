import sys
import pygame

FPS = 60

CUBE_SIZE = 90
PLAY_AREA_SIZE = CUBE_SIZE * 5

BACKGROUND_COLOR = (240, 240, 240)
BOARD_COLOR = (49, 32, 42)
PLAY_AREA_COLOR = (255, 255, 255)
CUBE_COLOR = (132, 122, 97)


def main():
    pygame.init()

    main_clock = pygame.time.Clock()

    window_surface = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('Quixo')
    window_surface.fill(BACKGROUND_COLOR)

    pygame.draw.circle(window_surface, BOARD_COLOR, (512, 384), 360)

    play_area_left = 512 - PLAY_AREA_SIZE / 2
    play_area_top = 384 - PLAY_AREA_SIZE / 2

    play_area = pygame.Rect(play_area_left, play_area_top, PLAY_AREA_SIZE, PLAY_AREA_SIZE)
    pygame.draw.rect(window_surface, PLAY_AREA_COLOR, play_area, 0, 5)

    for r in range(5):
        for c in range(5):
            cube_rect = pygame.Rect(play_area_left + CUBE_SIZE * r + 1, play_area_top + CUBE_SIZE * c + 1,
                                    CUBE_SIZE - 2, CUBE_SIZE - 2)
            pygame.draw.rect(window_surface, CUBE_COLOR, cube_rect, 0, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

        main_clock.tick(FPS)


if __name__ == '__main__':
    main()
