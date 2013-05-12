from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

py2exe_options = dict(
					excludes=['_ssl', 'doctest', 'pdb', 'difflib', 'inspect', 'calendar', 'pickle'],
					bundle_files=1,
					compressed=True,
					dll_excludes=['msvcr71.dll']




					 )

setup(
    options = {'py2exe': py2exe_options},
   	console = [{'script': "server.py"}],
    zipfile = None,
)