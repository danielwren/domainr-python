from setuptools import setup, find_packages

from domainr     import constants

def main():
    setup(
        name                = 'domainr',
        version             = constants.DOMAINR_PACKAGE_VERSION,
        author              = 'Daniel Wren',
        author_email        = 'daniel@danielwren.com',
        license             = 'MIT',
        description         = "Python wrapper / helper for the Domainr JSON API",
        long_description    = 'Domainr helps you explore the entire domain name space, including new gTLDs.',
        url                 = "http://domai.nr/",
        download_url        = 'https://github.com/danielwren/domainr-python/tarball/master',
        packages            = find_packages(),
        install_requires    = ['requests'],
        classifiers         = [
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],        
    )


if __name__ == '__main__':
    main()