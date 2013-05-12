import web
import json
import pySkypeResolver

urls = (
  '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
    	userName = web.input(_method='get')['userName']
    	resolve = pySkypeResolver.resolve(userName)
    	publicIp = resolve['publicIp']
    	localIp = resolve['localIp']
        return json.dumps({'publicIp': publicIp, 'localIp': localIp})
        return userName


if __name__ == "__main__": app.run()