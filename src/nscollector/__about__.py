__all__ = [
    '__author__', '__classifiers__', '__desc__', '__license__',
    '__package_name__', '__scripts__', '__url__', '__version__',
]

__author__ = 'Luke Powers'
# For more classifiers, see http://goo.gl/zZQaZ
__classifiers__ = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Utilities',
    'Private :: Do Not Upload'
    # Do not allow this package to be uploaded to pypi.python.org
]
__cli_name__ = 'ns-collector'
__desc__ \
    = '''Tool to scrape Nation States for stats'''
__license__ = 'Apache Software License 2.0'
__package_exclude__ = ['tests']
__requires__ = [
    'beautifulsoup',
    'django',
    'requests',
    ]
__scripts__ = []
__version__ = '0.0.1'
