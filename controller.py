import pygame

from model import Model
from view import View


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.running = True

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                grid_position = self.view.convert_to_grid(event.pos)
                if grid_position is not None:
                    row, col = grid_position
                    self.model.select_cube_at(row, col)
                else:
                    self.model.unselect_cube()

            # To make some "view-only" visual effects
            self.view.on_mouse_over(pygame.mouse.get_pos())

            self.view.update()
