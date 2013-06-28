import urllib2
import json
from urllib import urlencode


class SMSSendError(Exception):

    def __str__(self):
        return "Error sending SMS"


class SMSGate(object):
    """ Docstring! """
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def send(self, phone, message):
        params = {"phone": phone, "message": message}
        url = "%s?%s" % (self.endpoint, urlencode(params))
        opener = urllib2.urlopen(url)
        request = opener.read()
        result = json.loads(request)
        if result["status"] is False:
            raise SMSSendError
