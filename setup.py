import py2exe
from distutils.core import setup

setup(
    options = {'py2exe': {'bundle_files': 1}},
    windows = [{'script': "server.py"}],
    zipfile = None,
)
