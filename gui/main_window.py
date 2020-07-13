from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
from gui.constants import PADDING
from gui import SettingsWindow

SELECTED_FILES = "{selected} archivos seleccionados"
DEFAULT_REPORT_NAME = "reporte-{name}.{extension}"


def build_filename(name, extension):
    return DEFAULT_REPORT_NAME.format(name=name, extension=extension)


def select_all(event):
    end = event.widget.get().index('.')
    event.widget.select_range(0, end)
    event.widget.icursor('end')


class MainWindow(Frame):
    def __init__(self, master, settings, report_creator):
        super().__init__(master=master)
        self.settings = settings
        self.report_creator = report_creator
        self.list_of_files_selected = []

        self.report_name_label = Label(
            master=self.master,
            text="Nombre del Reporte:")

        self.format_label = Label(
            master=self.master,
            text="Formato del Reporte:")

        self.settings_button = Button(
            master=self.master,
            text="Ajustes",
            command=self.open_settings)

        self.selected_format = StringVar(
            master=self.master,
            value=self.report_creator.get_write_formats()[0])

        self.report_name = StringVar(
            master=self.master,
            value=build_filename(name=datetime.now().date(),
                                 extension=self.selected_format.get()))

        validate_report_name = self.master.register(self.validate_report_name)

        self.report_name_text_field = Entry(
            master=self.master, width=25,
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
            master=self.master,
            text="Seleccionar Evaluaciones",
            command=self.select_evaluations_handler)

        self.selected_files = StringVar(
            master=self.master,
            value=SELECTED_FILES.format(selected=0))

        self.selected_files_label = Label(
            master=self.master,
            textvariable=self.selected_files)

        self.create_report_button = Button(
            master=self.master,
            text="Crear Reporte",
            command=self.create_report_handler)

        self.setupUI()
        self.bind_events()

    def setupUI(self):
        self.report_name_label.pack(pady=PADDING, fill=X)
        self.report_name_text_field.pack(pady=PADDING, fill=X)
        self.format_label.pack(pady=PADDING, fill=X)

        for report_format in self.report_formats:
            report_format.pack(pady=PADDING, fill=X)

        self.select_evaluations_button.pack(pady=PADDING, fill=X)
        self.selected_files_label.pack(pady=PADDING, fill=X)
        self.create_report_button.pack(pady=PADDING, fill=X)
        self.settings_button.pack(pady=PADDING, fill=X)

    def bind_events(self):
        for event in ["<FocusIn>", "<Command-a>", "<Control-KeyRelease-a>"]:
            self.report_name_text_field.bind(event, select_all)

    def validate_report_name(self, report_name):
        selected_format = self.selected_format.get()

        return report_name.endswith(selected_format)

    def open_settings(self):
        SettingsWindow(self, self.settings)

    def select_evaluations_handler(self):
        files = filedialog.askopenfilenames()

        if len(files) == 0:
            return

        self.set_total_files_selected(len(files))
        self.list_of_files_selected = files

    def create_report_handler(self):
        if len(self.list_of_files_selected) == 0:
            return messagebox.showerror("Error", "No hay archivos seleccionados")

        self.report_creator.create(
            self.list_of_files_selected, self.report_name.get())

    def set_total_files_selected(self, total):
        self.selected_files.set(SELECTED_FILES.format(selected=total))

    def change_report_name_extension(self):
        if '.' in self.report_name.get():
            filename, _ = self.report_name.get().split('.')
        else:
            filename = self.report_name.get()

        new_filename = ".".join([filename, self.selected_format.get()])

        self.report_name.set(new_filename)
