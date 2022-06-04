import uuid
import flask


class TracingUtil:
    @staticmethod
    def generate_uuid(original_id=""):
        result = uuid.uuid4()

        if original_id:
            # Optional : include an original request id
            result = "{},{}".format(original_id, result)

        return result

    @staticmethod
    def generate_request_id():
        if getattr(flask.g, "request_id", None):
            return flask.g.request_id

        headers = flask.request.headers
        original_request_id = headers.get("X-Request-Id")
        new_uuid = TracingUtil.generate_uuid(original_request_id)
        flask.g.request_id = new_uuid

        return new_uuid
