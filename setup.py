import os
from setuptools import setup, find_packages
from setuptools.command.test import test
import sys


def _get_src_dir(package_name=None):
    '''Get the source directory by looking in src, or if package_name is
    given, return that combined with the src directory.

    '''
    ret = ''
    if 'PY_PACKAGE_NAME' in os.environ:
        ret = os.path.join(BASE_DIR, 'src', os.environ['PY_PACKAGE_NAME'])
    elif package_name:
        ret = os.path.join(BASE_DIR, 'src', package_name)
    if not ret:
        dirs_with_about = [dir for dir in os.listdir('src')
                           if '__about__.py' in os.listdir('src/'+dir)]
        if len(dirs_with_about) > 1:
            print 'More than one source with __about__.py defined, set PY_PACKAGE_NAME and re-run.'
            exit
        else:
            ret = os.path.join(BASE_DIR, 'src', dirs_with_about.pop())
    return ret


BASE_DIR = os.path.dirname(__file__)
SRC_DIR = _get_src_dir()
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
    author_email=about['__author_email__'],
    classifiers=about['__classifiers__'],
    cmdclass={'test': PyTest},
    description=about['__package_name__'].replace('_', ' ').title(),
    entry_points=about['__entry_points__'],
    install_requires=about['__requires__'],
    license=about['__license__'],
    long_description=about['__desc__'],
    name=about['__package_name__'],
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=['tests', 'tests.*']),
    platforms='any',
    scripts=about['__scripts__'],
    tests_require=['pytest'],
    url=about['__url__'],
    version=about['__version__'],
    zip_safe=False
)
