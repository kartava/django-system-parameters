class GreenText:
    DARK_GREEN = "\033[32m"
    ENDING = "\033[0m"

    def get_green_value(self, value):
        return f"{self.DARK_GREEN}{value}{self.ENDING}"


class ParametersDirectoryMixin:
    def get_parameters_dir(self):
        from django.conf import settings

        return (
            getattr(settings, "SYSTEM_PARAMS_DIR", None)
            or settings.BASE_DIR
        )
