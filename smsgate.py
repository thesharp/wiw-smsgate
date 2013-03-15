from xmlrpclib import ServerProxy


class SMSSendError(Exception):

    def __str__(self):
        return "Error sending SMS"


class SMSGate(object):
    """ Docstring! """
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.gate = ServerProxy(self.endpoint)

    def send(self, phone, message):
        result = self.gate.sms.send(phone, message)
        if result == "1":
            raise SMSSendError
