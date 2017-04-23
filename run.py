import sys

from app import app

port=5000

app.run(threaded=True, port=port)
