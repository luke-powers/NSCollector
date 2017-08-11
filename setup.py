import os
from setuptools import setup, find_packages
from setuptools.command.test import test
import sys

BASE_DIR = os.path.dirname(__file__)
PACKAGE_NAME = 'NSCollector'
SRC_DIR = os.path.join(BASE_DIR, "src", PACKAGE_NAME.lower())

about = {}
with open(os.path.join(SRC_DIR, "__about__.py")) as f:
    exec(f.read(), about)


class PyTest(test):
    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = [os.path.join(BASE_DIR, "tests")]
        self.test_suite = True

    def run_tests(self):
        # import here, since outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    author=about['__author__'],
    classifiers=about['__classifiers__'],
    cmdclass={'test': PyTest},
    description=PACKAGE_NAME.replace('_', ' ').title(),
    entry_points={
        'console_scripts':
        [
            '%(pkg_name_cli)s=%(pkg_name)s.__main__:main'
            % {
                'pkg_name_cli': about['__cli_name__'],
                'pkg_name': PACKAGE_NAME.lower()
            }
        ]
    },
    install_requires=about['__requires__'],
    license=about['__license__'],
    long_description=about['__desc__'],
    name=PACKAGE_NAME,
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=['tests', 'tests.*']),
    platforms='any',
    scripts=about['__scripts__'],
    tests_require=['pytest'],
    url='http://github.com/%s/%s' % (about['__author__'].replace(' ', '-'), PACKAGE_NAME),
    version=about['__version__'],
    zip_safe=False
)