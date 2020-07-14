from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from gui.constants import PADDING


class SettingsWindow(Toplevel):

    def __init__(self, master, settings):
        super().__init__(master)

        self.settings = settings
        self.max_points_frame = Frame(self)

        self.max_points_label = Label(
            self.max_points_frame, 
            text='Calificación Máxima por pregunta')

        self.max_points = IntVar(
            self.max_points_frame, 
            value=settings["max_points_per_question"])

        self.max_points_per_question_spinbox = Spinbox(
            self.max_points_frame, 
            textvariable=self.max_points, 
            from_=1, 
            to=100000)

        self.save_settings_button = Button(
            self, 
            text='Guardar', 
            command=self.save_settings)

        self.setup_ui()

    def setup_ui(self):
        self.max_points_frame.pack(
            fill=X)
        
        self.max_points_label.pack(
            pady=PADDING, 
            fill=X, 
            side=LEFT)

        self.max_points_per_question_spinbox.pack(
            pady=PADDING, 
            fill=X, 
            side=LEFT)

        self.save_settings_button.pack(
            pady=PADDING, 
            fill=X)

    def save_settings(self):
        self.export_settings()
        self.close()
    
    def export_settings(self):
        self.settings["max_points_per_question"] = self.max_points.get()

        self.settings.save()

    def close(self):
        self.destroy()
        self.update()
