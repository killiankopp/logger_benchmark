from time import sleep

from rich.console import Console
from rich.logging import RichHandler
import logging

console = Console(force_terminal=True)  # good for CI too
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console, show_time=True, show_level=True, show_path=False)]
)
log = logging.getLogger("app")

log.info("Server starting")
log.info("Server running")
sleep(1)
log.info("Server shutting down")
log.error("Server crashed")
sleep(1)
log.critical("Server killed")
log.warning("Server stopped")