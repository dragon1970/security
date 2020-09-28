#  https://pypi.org/project/whois/ 
#  environment: python wrap of linux whois
"""
>>> import whois
>>> domain = whois.query('google.com')

>>> print(domain.__dict__)
{
        'expiration_date': datetime.datetime(2020, 9, 14, 0, 0),
        'last_updated': datetime.datetime(2011, 7, 20, 0, 0),
        'registrar': 'MARKMONITOR INC.',
        'name': 'google.com',
        'creation_date': datetime.datetime(1997, 9, 15, 0, 0)
}

>>> print(domain.name)
google.com

>>> print(domain.expiration_date)
2020-09-14 00:00:00

"""

# https://pypi.org/project/python-whois/
# os independent
"""
$ pip install python-whois
>>> import whois
>>> w = whois.whois('webscraping.com')
>>> w.expiration_date  # dates converted to datetime object
datetime.datetime(2013, 6, 26, 0, 0)
>>> w.text  # the content downloaded from whois server
u'\nWhois Server Version 2.0\n\nDomain names in the .com and .net
...'

>>> print w  # print values of all found attributes
creation_date: 2004-06-26 00:00:00
domain_name: [u'WEBSCRAPING.COM', u'WEBSCRAPING.COM']
emails: [u'WEBSCRAPING.COM@domainsbyproxy.com', u'WEBSCRAPING.COM@domainsbyproxy.com']
expiration_date: 2013-06-26 00:00:00
...   
"""
