# Go sequentialy

# gcloud init
# gcloud components install app-engine-python
# gcloud components install app-engine-python-extras

# gcloud config set project YOUR_PROJECT_ID

# main.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World from Google App Engine!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


# requirements.txt
flask
gunicorn

#app.yaml
runtime: python39
entrypoint: gunicorn -b :$PORT main:app


# gcloud app deploy


