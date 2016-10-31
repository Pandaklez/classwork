from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body><p>Hello, world!</p></body></html>'

if __name__ == '__main__':
    app.run(debug=True)
