import json
from flask_restful import Resource
from flask import Response, request
from .join_controller import get_join


class JoinApi(Resource):
    def get(self):
        rs = get_join()
        rj = json.dumps(rs)
        return Response(rj, mimetype="application/json", status=rs['status'])