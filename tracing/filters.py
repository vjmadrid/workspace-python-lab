import logging
import flask

from src.common.tracing.util import TracingUtil


class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = TracingUtil.generate_request_id() if flask.has_request_context() else ""
        return True
