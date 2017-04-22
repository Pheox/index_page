import sys

from app import app

port = 5000

app.run(debug = True, threaded=True, port=port)
