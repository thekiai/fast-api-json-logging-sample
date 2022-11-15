import json
import logging
import sys
import traceback

class FormatterJSON(logging.Formatter):
    def format(self, record):
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)
        j = {
            "logLevel": record.levelname,
            "timestamp": f"{record.asctime}.{record.msecs}Z",
            "timestamp_epoch": record.created,
            "message": record.getMessage(),
            "module": record.module,
            "filename": record.filename,
            "funcName": record.funcName,
            "levelno": record.levelno,
            "lineno": record.lineno,
            "traceback": {},
            "extra_data": record.__dict__.get("extra_data", {}),
            "event": record.__dict__.get("event", {}),
        }
        if record.exc_info:
            exception_data = traceback.format_exc()
            j["traceback"] = exception_data

        return json.dumps(j, ensure_ascii=False)


def configure_logging():
    logger = logging.getLogger("uvicorn")
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    logger.setLevel(logging.DEBUG)
    formatter = FormatterJSON(
        "[%(levelname)s]\t%(asctime)s.%(msecs)dZ\t%(levelno)s\t%(message)s\n",
        "%Y-%m-%dT%H:%M:%S",
    )
    handler.setFormatter(formatter)
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(handler)
    logger.propagate = False
    return logger
