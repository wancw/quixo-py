from view import View


class Model:
    def __init__(self, view: View):
        self.view = view

        self.board = tuple(
            tuple(
                (r * 5 + c + 1, '_')
                for c in range(5)
            )
            for r in range(5)
        )
        self.selected_cube = None

    def select_cube_at(self, row, col):
        self.unselect_cube()

        self.selected_cube = self.board[row][col]
        cube_id = self.selected_cube[0]
        self.view.select_cube(cube_id)

    def unselect_cube(self):
        if self.selected_cube is not None:
            cube_id = self.selected_cube[0]
            self.selected_cube = None
            self.view.unselect_cube(cube_id)
