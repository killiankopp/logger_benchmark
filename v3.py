from loguru import logger
from rich.console import Console
from rich.logging import RichHandler
import logging, json, sys

# Human stream via stdlib + Rich
logging.basicConfig(level="INFO", handlers=[RichHandler()], format="%(message)s")

# Machine stream via Loguru JSON
def json_sink(msg):
    rec = msg.record
    print(json.dumps({"t": rec["time"].isoformat(), "lvl": rec["level"].name, "msg": rec["message"]}), file=sys.stderr)

logger.add(json_sink, level="INFO")

# Use both:
logging.getLogger("ui").info("Started UI")
logger.bind(request_id="r-7").info("API ready")

logger.bind(request_id="r-8").critical("API not ready")
logging.getLogger("ui").error("Stopped UI")