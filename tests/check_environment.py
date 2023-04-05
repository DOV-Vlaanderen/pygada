# This script is adapted from
# https://github.com/jorisvandenbossche/ICES-python-data/blob/main/check_environment.py
# which originates from the script from Andreas Mueller:
# https://github.com/amueller/scipy-2018-sklearn/blob/master/check_env.ipynb
# and glemaitre: https://github.com/glemaitre/pyparis-2018-sklearn/blob/master/check_environment.py

from __future__ import print_function
from packaging.version import Version
from packaging import version
from importlib.metadata import version as meta_version
import sys

try:
    import curses
    curses.setupterm()
    assert curses.tigetnum("colors") > 2
    OK = "\x1b[1;%dm[ OK ]\x1b[0m" % (30 + curses.COLOR_GREEN)
    FAIL = "\x1b[1;%dm[FAIL]\x1b[0m" % (30 + curses.COLOR_RED)
except:
    OK = '[ OK ]'
    FAIL = '[FAIL]'

try:
    import importlib
except ImportError:
    print(FAIL, "Python version 3.4 is required,"
                " but %s is installed." % sys.version)


def import_version(pkg, min_ver, fail_msg=""):
    mod = None
    try:
        mod = importlib.import_module(pkg)
        if pkg in {'PIL'}:
            ver = mod.VERSION
        elif pkg in {'xlrd'}:
            ver = mod.__VERSION__
        else:
            try:
                ver = mod.__version__
            except AttributeError:
                ver = meta_version(pkg)
        if Version(ver) < version.parse(min_ver):
            print(FAIL, "%s version %s or higher required, but %s installed."
                  % (lib, min_ver, ver))
        else:
            print(OK, '%s version %s' % (pkg, ver))
    except ImportError:
        print(FAIL, '%s not installed. %s' % (pkg, fail_msg))
    return mod


# first check the python version
print('Using python in', sys.prefix)
print(sys.version)
pyversion = version.parse(sys.version.split('|')[0])
if pyversion >= version.parse("3.0.0"):
    if pyversion < version.parse("3.6.0"):
        print(FAIL, "Python version 3.6 is required,"
                    " but %s is installed." % sys.version)
else:
    print(FAIL, "Python 3 is required, but %s is installed." % sys.version)

print()
requirements = {'fiona': '1.8.22',
                'geocube': '0.3.3',
                'geopandas': '0.10.2',
                'IPython': '8.11.0',
                'jupyter': '1.0.0',
                'jupyterlab': '3.6.1',
                'loguru': '0.6.0',
                'matplotlib': '3.6.1',
                'numpy': '1.23.4',
                'owslib': '0.27.2',
                'pandas': '1.5.0',
                'pydov': '2.2.3',
                'pyproj': '3.4.0',
                'pysgems': '1.2.3',
                'rasterio': '1.3.3',
                'scipy': '1.9.1',
                'seaborn': '0.11.2',
                }


# now the dependencies
for lib, required_version in list(requirements.items()):
    import_version(lib, required_version)
