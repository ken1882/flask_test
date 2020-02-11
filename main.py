from flask import Flask, request, jsonify

AppName = "FlaskTest"

def create_app():
  return Flask(AppName)

app = create_app()

@app.route("/")
def index():
  return "Hello World!"

if __name__ == "__main__":
  app.run()