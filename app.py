import falcon
import uuid
import json


class UuidResource:
    def on_get(self, req, resp):
        body = {'uuid': str(uuid.uuid4())}
        resp.media = body

api = falcon.API()
api.add_route('/uuid', UuidResource())
