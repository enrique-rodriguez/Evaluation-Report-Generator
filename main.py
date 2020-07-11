from configuration import settings
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

from datetime import datetime

PADDING = 5
SELECTED_FILES = "{selected} archivos seleccionados"


class CreateReportController(Frame):
    def __init__(self, master, report_creator):
        super().__init__(master=master)
        self.report_creator = report_creator

        self.report_name_label = Label(
            self.master, text="Nombre del reporte")

        self.report_name = StringVar(
            self.master, value=f'reporte-{datetime.now().date()}.xlsx')

        self.report_name_text_field = Entry(
            self.master, width=25, textvariable=self.report_name)

        self.selected_format = StringVar(
            value=self.report_creator.get_write_formats()[0])

        self.report_formats = [
            Radiobutton(
                master=self.master,
                variable=self.selected_format,
                value=file_format,
                text=file_format
            ) for file_format in self.report_creator.get_write_formats()
        ]

        self.select_evaluations_button = Button(
            self.master, text="Seleccionar Evaluaciones", command=self.select_evaluations_handler)

        self.selected_files = StringVar(
            value=SELECTED_FILES.format(selected=0))

        self.selected_files_label = Label(
            self.master, textvariable=self.selected_files)

        self.create_report_button = Button(
            self.master, text="Crear Reporte")

        self.setupUI()

    def setupUI(self):
        self.report_name_label.pack(pady=PADDING)
        self.report_name_text_field.pack(pady=PADDING)

        for report_format in self.report_formats:
            report_format.pack(pady=PADDING)

        self.select_evaluations_button.pack(pady=PADDING)
        self.selected_files_label.pack(pady=PADDING)
        self.create_report_button.pack(pady=PADDING)

    def select_evaluations_handler(self):
        files = filedialog.askopenfilenames()

        self.set_total_files_selected(len(files))

    def set_total_files_selected(self, total):
        self.selected_files.set(SELECTED_FILES.format(selected=total))


if __name__ == "__main__":
    root = Tk()

    root.title("Generador de Reportes de Evaluación")
    root.geometry("350x200")

    app = CreateReportController(
        master=root,
        report_creator=settings.container.get("CreateReport")
    )

    mainloop()
