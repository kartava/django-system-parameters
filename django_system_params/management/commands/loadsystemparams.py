import json
import logging
from django.core.management.base import BaseCommand

from ...models import SystemParam
from ...mixins import ParametersDirectoryMixin

logger = logging.getLogger(__name__)


class Command(BaseCommand, ParametersDirectoryMixin):
    help = """Load system parameters. """

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            default=f"{self.get_parameters_dir()}/system_params.json",
        )

    def handle(self, *args, **options):
        path = options.get("path")
        logger.info(
            f"Loading system parameters from \033[32m{path}\033[0m 🚀🚀🚀"
        )
        with open(path) as json_data:
            params = json.loads(str(json_data.read()))
        for param in params:
            instance, created = SystemParam.objects.update_or_create(
                name=param["name"],
                defaults={
                    "value": param["value"],
                },
            )
            logger.info(f"SystemParam: {instance.name} => created={created}")
        logger.info("System parameters loaded 💅💅💅")
