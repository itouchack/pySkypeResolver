#!/usr/bin/python2
#! -*- coding: utf-8 -*-
#
# ---------------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 43.5):
# @__akiaki wrote this file. As long as you retain this notice you can do whatever
# you want with this stuff. If we meet some day, and you think this stuff is worth
# it, you can buy me a beer (or caffeinated beverage) in return. --aki
# ---------------------------------------------------------------------------------
import web
import json
import time
import glob
import logparse
import skypeapi

urls = (
  '/', 'index',
  '/api/(.*)', 'api'
)

app = web.application(urls, globals())
render = web.template.render('templates/')
skypeapi.init()
logfile = glob.glob('*.log')[0]

class api:
    def GET(self, username):
        skypeapi.activateSkype(username)
        time.sleep(1) # because skype is ew
        return json.dumps(logparse.search(logfile, username))

class index:
    def GET(self):
        return render.index()

if __name__ == "__main__":
    app.run()
