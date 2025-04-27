from flask import Flask


app = Flask(__name__)

@app.route('/')
def default():
    return 'Hello World!!'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8999,debug=True)

