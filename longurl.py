#!/usr/bin/python

import httplib
from urlparse import urlparse

__author__ = 'David Lynch (kemayo at gmail dot com)'
__version__ = '0.1'
__copyright__ = 'Copyright (c) 2010 David Lynch'
__license__ = 'New BSD License'

URLCACHE = {}

def longurl(url):
    """Expands a URL, if possible
    
    If a non-http/https URL is provided it returns False
    If the URL has no Location header, the original URL is returned
    Repeated requests for the same URL are cached, and will not
        cause further HTTP requests
    """
    if url in URLCACHE:
        return URLCACHE[url]
    o = urlparse(url, 'http')
    if not o.scheme in ('http', 'https'):
        return False
    
    conn = httplib.HTTPConnection(o.netloc)
    conn.request('HEAD', "%s%s%s" % (o.path, o.params and ';'+o.params, o.query and '?'+o.query))
    response = conn.getresponse()
    URLCACHE[url] = response.getheader('location') or url
    return URLCACHE[url]


if __name__ == "__main__":
    print longurl('http://bit.ly/bZtfbX')
    print longurl('http://adf-fuensalida.deviantart.com/art/Gender-Police-on-my-DA-NEIN-164806087')