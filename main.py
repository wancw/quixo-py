from controller import Controller
from model import Model
from view import View

if __name__ == '__main__':
    view = View()
    model = Model(view)
    controller = Controller(model, view)
    while controller.running:
        controller.process_input()
        view.draw()
