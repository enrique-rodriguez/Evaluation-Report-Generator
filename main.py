from tkinter import *
from tkinter.ttk import *

from configuration import settings

from gui import MainWindow

if __name__ == "__main__":
    root = Tk()

    style = Style()
    style.configure('TButton',
                    font=('Times', 18))
    style.configure('TLabel',
                    font=('Times', 18))
    style.configure('TRadioButton',
                    font=('Times', 18))

    root.title("Generador de Reportes")
    root.geometry("300x250")
    root.resizable(False, False)

    app = MainWindow(
        master=root,
        settings=settings.config,
        report_creator=settings.container.get("CreateReport")
    )

    root.mainloop()
