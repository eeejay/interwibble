from distutils.core import setup

interwibble_dict = {}
execfile('interwibble', interwibble_dict)

setup(
    name         = 'interwibble',
    version      = interwibble_dict['VERSION'],
    description  = interwibble_dict['__doc__'],
    author       = 'Eitan Isaacson',
    author_email = 'eitan@monotonous.org',
    url          = 'http://monotonous.org/',
    license      = 'GPL',
    classifiers  = ['Development Status :: 3 - Alpha',
                    'Environment :: Console',
                    'Intended Audience :: End Users/Desktop',
                    'Intended Audience :: Information Technology',
                    'License :: OSI Approved :: GNU General Public License (GPL)',
                    'Operating System :: POSIX',
                    'Programming Language :: Python',
                    'Topic :: Internet :: WWW/HTTP',
                    'Topic :: Text Processing :: Markup :: HTML'
                    ],
    scripts      = ['interwibble']
    )
