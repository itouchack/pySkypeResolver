import web
import json
import pySkypeResolver

urls = (
  '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
    	userName = web.input(_method='get')
    	resolve = pySkypeResolver.resolve(userName)
    	publicIp = resolve['publicIp']
    	localIp = resolve['localIp']
        return json.dumps({'publicIp': publicIp, 'localIp': localIp})


if __name__ == "__main__": app.run()