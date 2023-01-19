import os
import json
import logging
from django.core.management.base import BaseCommand

from ...mixins import ParametersDirectoryMixin, GreenText

logger = logging.getLogger(__name__)

EXAMPLE_PARAMS = [
    {"name": "REQUEST_LIMIT", "value": 500},
    {"name": "BASE_FEE", "value": 0.9},
    {"name": "ENABLE_SOME_FEATURE", "value": True},
    {"name": "SYSTEM_USER_EMAIL", "value": "system.user@mail.com"},
    {
        "name": "PHONE_COUNTRY_CODES",
        "value": {"ae": "971", "de": "49", "ua": "380", "us": "1"},
    },
    {"name": "SKIP_IDS", "value": [1, 2, 3]},
]


class Command(BaseCommand, ParametersDirectoryMixin, GreenText):
    help = """Create example file with system parameters. """

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            default=f"{self.get_parameters_dir()}/system_params.json",
        )

    def handle(self, *args, **options):
        logger.info("Creating system parameters file 🚀🚀🚀")
        path = options.get("path")

        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as outfile:
                outfile.write(json.dumps(EXAMPLE_PARAMS, indent=4))
            logger.info(
                f"System parameters example "
                f"is available under: {self.get_green_value(path)}"
            )
        else:
            logger.info(
                f"System parameters file "
                f"is already exists under: {self.get_green_value(path)}"
            )
