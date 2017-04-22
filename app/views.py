from app import app

@app.route('/')
def page():
  return 'Hello World'
