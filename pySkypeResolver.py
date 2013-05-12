import Skype4Py
import sys
import pyResolve
import glob
from time import sleep
def resolve(skypeName):
	try:
		skype = Skype4Py.Skype()
		skype.Attach()
		skype.Client.Focus()
		skype.Client.OpenUserInfoDialog(skypeName)
		skype.Client.Minimize()
		skype.Client.Focus()
		sleep(1)
		resolving = pyResolve.search(glob.glob('*.log')[0], skypeName)
		publicIp = resolving[0]['public']
		localIp = resolving[0]['local']
		return { 'success': True, 'publicIp': publicIp, 'localIp': localIp }
	except:
		return { 'success': False, 'publicIp': 'Fail.', 'localIp': 'Fail' }