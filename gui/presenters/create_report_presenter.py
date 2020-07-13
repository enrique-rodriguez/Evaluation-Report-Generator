from tkinter import messagebox

from report_generator.usecases.port.presenter import CreateReportPresenter


class TkinterCreateReportPresenter(CreateReportPresenter):

    def present(self, errors, total_written):
        title = "Reporte creado"
        message = f"{total_written} evaluaciones escritas exitosamente"

        if len(errors) > 0:
            message += self.get_error_message(errors)

        messagebox.showinfo(title, message)

    def get_error_message(self, errors):
        message = "\nOcurrieron los siguientes errores:\n"

        for file, error in errors.items():
            message += f"{file}: {error}\n"

        return message
