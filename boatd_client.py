from __future__ import print_function

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

import json

class Boat(object):
    def __init__(self, host='localhost', port=2222):
        self.host = host
        self.port = port

    def _url(self, endpoint):
        return 'http://{}:{}{}'.format(self.host, self.port, endpoint)

    def _get(self, endpoint):
        json_body = urlopen(self._url(endpoint)).read()
        return json.loads(json_body)

    def heading(self):
        content = self._get('/heading')
        return content.get('result')

    def wind(self):
        content = self._get('/wind')
        return content.get('result')

    def position(self):
        content = self._get('/position')
        return tuple(content.get('result'))

if __name__ == '__main__':
    boat = Boat()
    print(boat._get(''))
    print(boat.heading())
    print(boat.wind())
    print(boat.position())
