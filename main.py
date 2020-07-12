from tkinter import *
from tkinter.ttk import *

from configuration import settings
from gui import MainWindow

if __name__ == "__main__":
    root = Tk()

    root.title("Generador de Reportes")
    root.geometry("300x300")
    root.resizable(False, False)

    app = MainWindow(
        master=root,
        settings=settings.config,
        report_creator=settings.container.get("CreateReport")
    )

    mainloop()
