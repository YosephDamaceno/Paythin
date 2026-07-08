from model import classes
from Controller.controller import Controller
from View.view import View

def main():
    model = classes.Desenho()
    view = View()
    controller = Controller(view)

    view.iniciar()

if __name__ == "__main__":
    main()