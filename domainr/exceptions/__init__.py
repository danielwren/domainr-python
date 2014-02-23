class KeyError(Exception):
    ''' This error is used to be raised on invalid Domainr API key '''
    
    message = "In order to query against Domainr you will need to provide valid Domainr key."

    def __init__(self, error_code=None, http_code=None):
        Exception.__init__(self, self.message)
        self.message    = self.message
        self.error_code = error_code
        self.http_code  = http_code
        

class DomainError(Exception):
    ''' This error is used to be raised on invalid domain '''

    message = "Invalid domain name provided"

    def __init__(self, error_code=None, http_code=None):
        Exception.__init__(self, self.message)
        self.message    = self.message
        self.error_code = error_code
        self.http_code  = http_code
        

class RequestTypeError(Exception):
    ''' This error is used to be raised on invalid Domainr request type '''

    message = "Invalid request type provided"

    def __init__(self, error_code=None, http_code=None):
        Exception.__init__(self, self.message)
        self.message    = self.message
        self.error_code = error_code
        self.http_code  = http_code


class ResponseError(Exception):
    ''' This error is used to be raised on Domainr error '''

    def __init__(self, message='', error_code=None, http_code=None):
        Exception.__init__(self, message)
        self.message    = message
        self.error_code = error_code
        self.http_code  = http_code
        
        