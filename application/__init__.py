from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', context={'teste': 'Oba'})

@app.route('/corrego/<int:corrego_id>', methods=['GET'])
def corrego_endpoint(corrego_id):
    return render_template('index.html', context={'teste': 'ObaGet {}'.format(corrego_id)})

