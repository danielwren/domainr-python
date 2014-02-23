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