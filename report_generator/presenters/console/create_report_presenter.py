from report_generator.usecases.port.presenter import CreateReportPresenter


class ConsoleCreateReportPresenter(CreateReportPresenter):

    def present(self, errors, total_written):
        print(f"{total_written} evaluation file/s written")

        if len(errors) > 0:
            self.report_errors(errors)

    def report_errors(self, errors):
        print(f"{len(errors)} error/s occurred:")

        for file, error in errors.items():
            print(f"{file}: {error}")
