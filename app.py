from flask import Flask

# app = Flask(__name__)

app = Flask(__name__, static_url_path='/', static_folder='_build/html/')

# code from SO post
# @app.route('/<path:path>')
@app.route('/')
def serve_sphinx_docs(path='index.html'):
    return app.send_static_file(path)
# def hello_world():
#     return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
