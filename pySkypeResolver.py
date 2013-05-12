import Skype4Py
import sys
import pyResolve
import socket
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
		resolving = pyResolve.search('debug-20130512-0558.log', skypeName)
		publicIp = resolving[0]['public']
		localIp = resolving[0]['local']
		return { 'success': True, 'publicIp': publicIp, 'localIp': localIp }
	except socket.error:
		print('Usage: \n	pySkypeResolver.py <SKYPEUSERNAME>')
		print('Example: \n	pySkypeResolver.py echo123')
		print('\nThe client flickering is for a 24/7 resolve.\n')
		print('Make sure you have Skype running and that this script is able to attach to your skype.')
		return { 'success': False, 'publicIp': 'Fail.', 'localIp': 'Fail' }