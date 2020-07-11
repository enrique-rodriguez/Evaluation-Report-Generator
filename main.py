from configuration import settings
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

from datetime import datetime

PADDING = 5
SELECTED_FILES = "{selected} archivos seleccionados"
DEFAULT_REPORT_NAME = "reporte-{name}.{extension}"


def build_filename(name, extension):
    return DEFAULT_REPORT_NAME.format(name=name, extension=extension)


def select_all(event):
    end = event.widget.get().index('.')
    event.widget.select_range(0, end)
    event.widget.icursor('end')


class CreateReportController(Frame):
    def __init__(self, master, report_creator):
        super().__init__(master=master)
        self.report_creator = report_creator

        self.report_name_label = Label(
            self.master, text="Nombre del reporte")

        self.format_label = Label(
            self.master, text="Formato del reporte")

        self.selected_format = StringVar(
            value=self.report_creator.get_write_formats()[0])

        self.report_name = StringVar(
            self.master,
            value=build_filename(name=datetime.now().date(), extension=self.selected_format.get()))

        validate_report_name = self.master.register(self.validate_report_name)
        self.report_name_text_field = Entry(
            self.master, width=25,
            textvariable=self.report_name,
            validate='key',
            validatecommand=(validate_report_name, '%P'))

        self.report_formats = [
            Radiobutton(
                master=self.master,
                variable=self.selected_format,
                value=file_format,
                text=file_format,
                command=self.change_report_name_extension
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
        self.bind_events()

    def setupUI(self):
        self.report_name_label.pack(pady=PADDING)
        self.report_name_text_field.pack(pady=PADDING)
        self.format_label.pack(pady=PADDING)

        for report_format in self.report_formats:
            report_format.pack(pady=PADDING)

        self.select_evaluations_button.pack(pady=PADDING)
        self.selected_files_label.pack(pady=PADDING)
        self.create_report_button.pack(pady=PADDING)

    def bind_events(self):
        for event in ["<FocusIn>", "<Command-a>", "<Control-KeyRelease-a>"]:
            self.report_name_text_field.bind(event, select_all)

    def validate_report_name(self, report_name):
        selected_format = self.selected_format.get()

        return report_name.endswith(selected_format)

    def select_evaluations_handler(self):
        files = filedialog.askopenfilenames()

        self.set_total_files_selected(len(files))

    def set_total_files_selected(self, total):
        self.selected_files.set(SELECTED_FILES.format(selected=total))

    def change_report_name_extension(self):
        if '.' in self.report_name.get():
            filename, _ = self.report_name.get().split('.')
        else:
            filename = self.report_name.get()

        new_filename = ".".join([filename, self.selected_format.get()])

        self.report_name.set(new_filename)


if __name__ == "__main__":
    root = Tk()

    root.title("Generador de Reportes")
    root.geometry("350x300")

    app = CreateReportController(
        master=root,
        report_creator=settings.container.get("CreateReport")
    )

    mainloop()
