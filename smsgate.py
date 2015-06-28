import urllib2
import json


class SMSSendError(Exception):

    def __str__(self):
        return "Error sending message"


class SMSGate(object):
    """ Docstring! """
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def send(self, phone, message, telegram=False):
        params = {"phone": phone, "message": message}
        if telegram:
            params["telegram"] = True
        request = urllib2.Request(self.endpoint)
        result = json.loads(urllib2.urlopen(request, json.dumps(params)).read())
        if result["error"]:
            raise SMSSendError
