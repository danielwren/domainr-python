
import os, logging, re, json, requests
from domainr import exceptions, constants

class Domainr(object):

    def __init__(self, apiKey=''):
        self._apiKey = apiKey   # Coming 09/2014
    
    ###### Public Functions ######
    
    ### API Call Wrappers ###
    
    def search(self, domain):
        return self._query('search', domain)
        
    def info(self, domain):
        return self._query('info', domain)
        
    
    ### Convenience Functions ###    
        
    def isDomainAvailable(self, domain):
        
        # taken: the domain is already registered.
        # unavailable: registration of the domain isn't permitted, e.g. foo.uk.
        # maybe: the TLD is likely wildcarded, so you'll need to check manually.
        # tld: the item is a TLD, e.g. com or io.

        available = None
        content = self._query('info', domain)
        
        if(content['availability'] == 'taken' or 
            content['availability'] == 'unavailable' or
            content['availability'] == 'tld'): 
                
            available = False
        
        elif(content['availability'] == 'maybe'):
            available = None
            
        elif(content['availability'] == 'available'): 
            available = True
            
        else:
            raise exceptions.ResponseError("Unknown availability type received from API")
        
        return available
        
    
    
    ###### Private Functions ######
    
    def _query(self, *args, **kwargs):
        # args[0] - request type
        # args[1] - domain

        if not args[0] in constants.DOMAINR_REQUEST_TYPES:
            raise exceptions.RequestTypeError('Invalid request type provided')
        
        requestParams = self._getRequestParams(*args, **kwargs)
        request = requests.get(
            constants.DOMAINR_BASE_URL + args[0],   #e.g. http://domai.nr/api/json/ + info
            params=requestParams)

        logging.debug("[Domainr.query] Request URL : %s" % request.url)
        logging.debug("[Domainr.query] Response Status Code : %s" % request.status_code)
        logging.debug("[Domainr.query] Response Content : %s" % request.content)

        content = json.loads(request.content)

        try:
            errorCode = content['error']['status']
            errorMessage = content['error']['message']
            logging.debug("[Domainr.query] Error found in query response")
            raise exceptions.ResponseError(errorMessage, error_code=errorCode)
            
        except (KeyError, AttributeError) as e:
            logging.debug("[Domainr.query] No error found in query response")
        
        return content
        

    def _getRequestParams(self, *args, **kwargs):
        requestParams = {}
        
        # Required - Implicit arguments
        # if(self.validate('apikey', self._apiKey)):
        #     requestParams[''] = self._apiKey

        # Required - domain argument       
        if(self._validate('q', args[1])):
            requestParams['q'] = args[1]
            
        # Optional - Dictionary arguments
        for key, value in kwargs.iteritems():
            if(key in constants.DOMAINR_OPTIONAL_PARAMS):
                if(value is not None):
                    if(self._validate(key, value)):
                        requestParams[key] = value
        return requestParams
        
        
    
    ### Validation ###
    
    def _validate(self, param, value):

        # if(param == 'apikey'):
        #     isApiKeyValid = self._isValidApiKey(value)
        #     logging.debug("[Domainr.validate] Is API key valid? (%s)" % isApiKeyValid)
        #     if not isApiKeyValid:
        #         raise exceptions.KeyError('In order to query against Domainr you will need to provide valid Domainr key.')
        #     else:
        #         return True

        if(param == 'q'):
            isDomainValid = self._isValidDomain(value)
            logging.debug("[Domainr.validate] Is domain valid? (%s)" % isDomainValid)
            if not isDomainValid:
                raise exceptions.DomainError('In order to query against Domainr you will need to provide valid domain.')
            else:
                return True
                
        elif(param == 'callback'):
            # TODO - Add validation checks - does function exist?
            return True
            
        else:
            # TODO - Raise error
            pass

    
    
    # def _isValidApiKey(self, apikey):
    #     pass       


    def _isValidDomain(self, domain):

        logging.debug("[Domainr.is_valid_domain] Looking if %s is valid or not ..." % domain)
        # TODO - Make the G/TLD portion of the regex smarter
        domain_regex = re.compile(r'^(?=.{4,255}$)([a-zA-Z0-9][a-zA-Z0-9-]{,61}[a-zA-Z0-9]\.)+[a-zA-Z0-9]{2,}$')
                                    
        match = re.match(domain_regex, domain)
        if match: return True
        return False
        
        