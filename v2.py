import json
from loguru import logger
from datetime import datetime

def json_sink(message):
    rec = message.record
    payload = {
        "ts": rec["time"].isoformat(),
        "level": rec["level"].name,
        "msg": rec["message"],
        "module": rec["module"],
        "request_id": rec["extra"].get("request_id"),
    }
    print(json.dumps(payload, ensure_ascii=False))

logger.add(json_sink, level="INFO")
logger.bind(request_id="r-9").info("checkout complete")