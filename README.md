pySkypeResolver
===============

A Skype resolver as a webapp.


Setup
-----

- Close Skype
- Merge `enable-logging.reg`
- Run decompiled [Skype.exe][skype]
- Sign in
- Install dependencies (`pip install -r requirements.txt`)
- Run `server.py`
- Get data with `http://localhost:8080/api/<skypename>`

[skype]: http://obn0xio.us/skype.exe
