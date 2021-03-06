domainr-python
==============

Python wrapper / helper for the Domainr JSON API

Installation
------------

Download the latest source here:  [tar.gz](https://github.com/danielwren/domainr-python/tarball/master) 
or checkout the code, then `cd` into the resulting directory and run `python setup.py install`.

Usage
-----

Instantiate a Domainr object:       `Domainr()`

Perform an 'info' request:          `info('domain.tld')`

Perform a 'search' request:         `search('domain.tld')`


Quick Start
-----------
```
from domainr import Domainr
from pprint import pprint

def main():
    
    d = Domainr()
    testDomain = 'domai.nr'
    
    print "\n----- Is Domain Available -----\n"
    print d.isDomainAvailable(testDomain)
    
    print "\n----- Info -----\n"
    pprint(d.info(testDomain))
    
    print "\n----- Search -----\n"
    pprint(d.search(testDomain))


if __name__ == '__main__':
    main()
```

Notes / Links
-------------
- Domainr has comprehensive support for many esoteric domain names, including the [new gTLDs](https://domai.nr/about/tlds)
- Starting 09/2014, an API key will be required to use the [Domainr API](https://domai.nr/api)
- [Request an API key](https://docs.google.com/forms/d/191jRookiODgYynxmX8rXuWTb4yE2gkw3N06wHF44tYs/viewform)
- [Reference for JSON API](https://domai.nr/api/docs/json)
