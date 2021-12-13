import logging
from rich.logging import RichHandler


__name__ = "operator"
__version__ = "0.1.0"

# Set up logging
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    handlers=[RichHandler(rich_tracebacks=True, show_time=True, log_time_format="%Y %m %d %H %M %S")],
)

logging.getLogger(__name__).addHandler(logging.NullHandler())
