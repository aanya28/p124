from flask import Flask

app = Flask(__name__)

#specifies the route
@app.route("/demo")

def demo():
    return 'hello'

if __name__ == '__main__':
    app.run()