__all__ = [
    '__author__', '__classifiers__', '__desc__', '__license__',
    '__package_name__', '__scripts__', '__url__', '__version__',
]

__author__ = 'Luke Powers'
__author_email__ = 'luke-powers@users.noreply.github.com'
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
__desc__ = '''Tool to scrape Nation States for stats'''
__entry_points__ = {
    'console_scripts':
    [
        'ns-collector=nscollector.__main__:main',
    ]
}
__license__ = 'Apache Software License 2.0'
__package_exclude__ = ['tests']
__package_name__ = 'NSCollector'
__requires__ = [
    'pip>=9.0',
    'beautifulsoup',
    'django',
    'requests',
    ]
__scripts__ = []
__url__ = 'http://github.com/%s/%s' % (__author__.replace(' ', '-'), __package_name__)
__version__ = '0.0.1'
