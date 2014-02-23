from domainr import Domainr
import pprint

def main():
    
    d = Domainr()
    testDomain = 'domai.nr'
    
    print "\n----- Is Domain Available -----\n"
    print d.isDomainAvailable(testDomain)
    
    print "\n----- Info -----\n"
    pprint.pprint(d.info(testDomain))
    
    print "\n----- Search -----\n"
    pprint.pprint(d.search(testDomain))


if __name__ == '__main__':
    main()