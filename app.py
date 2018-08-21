import falcon
import uuid
import json
from datetime import datetime


class UuidResource:
    def on_get(self, req, resp):
        # body = {'uuid': str(uuid.uuid4())}
        body = {'uuid': str(uuid.uuid4()),
                'timestamp': str(datetime.now())}
        resp.media = body

api = falcon.API()
api.add_route('/uuid', UuidResource())
