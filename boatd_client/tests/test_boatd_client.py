from httpretty import HTTPretty, httprettified

from boatd_client import Boat

@httprettified
class TestBoatdClient(object):
    def setup(self):
        self.boat = Boat()

    def test_root(self):
        HTTPretty.register_uri(HTTPretty.GET, 'http://localhost:2222/',
                               body='{"boatd": {"version": "0.1mock"}}')
        assert self.boat.version()
