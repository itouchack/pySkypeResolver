import Skype4Py
import sys
from time import sleep
def resolve(skypeName):
	try:
		skype = Skype4Py.Skype()
		skype.Attach()
		skype.Client.OpenUserInfoDialog(sys.argv[1])
		skype.Client.Minimize()
		skype.Client.Focus()
		sleep(1)

		return { 'success': True, 'publicIp': publicIp, 'localIp': localIp }
	except:
		print('Usage: \n	pySkypeResolver.py <SKYPEUSERNAME>')
		print('Example: \n	pySkypeResolver.py echo123')
		print('\nThe client flickering is for a 24/7 resolve.\n')
		print('Make sure you have Skype running and that this script is able to attach to your skype.')
		return { 'success': False, 'publicIp': 'Fail.', 'localIp': 'Fail' }