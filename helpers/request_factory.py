from flask import Flask


class RequestFactory:
    @staticmethod
    def register_headers(app: Flask):
        @app.after_request
        def add_headers(response):
            response.headers["Access-Control-Allow-Origin"] = "*"
            response.headers[
                "Access-Control-Allow-Headers"
            ] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
            response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, DELETE, OPTIONS"
            return response

        return app
