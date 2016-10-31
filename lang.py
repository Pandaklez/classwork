from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    f = open('коды.txt', 'r', encoding = 'UTF-8')
    langlist = f.readlines()
    languages = {}
    for iso in langlist:
        iso = iso.split('.')
        languages[iso[0]] = iso[1]
    return render_template('index.html', languages = languages)

if __name__ == '__main__':
    app.run(debug = True)
