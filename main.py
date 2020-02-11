from flask import Flask

AppName = "FlaskTest"

def create_app():
  return Flask(AppName)

app = create_app()

@app.route("/")
def index():
  return "Hello World!"
