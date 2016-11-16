"""This file will be run when the catridge is started."""

# OVERWRITE THIS FILE

# test code:

import os

import bottle


PAGE = """<HTML>
    <HEAD>
        <TITLE>Server ready.</TITLE>
    </HEAD>
    <BODY>
        <h1>Success</h1>
        <p>You can now run your own python webserver with websocket support here.</p>
    </BODY>
</HTML>
"""

@bottle.get("/")
def mainpage():
    """shows the mainpage."""
    return PAGE


if __name__ == "__main__":
    host = os.getenv("OPENSHIFT_DIY_IP", "0.0.0.0")
    port = int(os.getenv("OPENSHIFT_DIY_PORT", 8000))
    bottle.run(host=host, port=port)
