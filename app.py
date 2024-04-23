import urllib.parse
from flask import *
from pathops import PathManipulator
import os
import html 
import urllib
import socket
import subprocess

app = Flask(__name__)

FOLDER_MAIN = 'X:/OrganicByALAKHPANDEY'

SERVER_STARTED = False 
# with open('server.prop.state','r') as f:
#     SERVER_STARTED = True if f.read().strip() == '1' else False

if not SERVER_STARTED:
    # Check if port 6969 is in use
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', 6969))
    if result != 0:
        subprocess.Popen(['python', '-m', 'http.server', '6969', '--directory', FOLDER_MAIN], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        SERVER_STARTED = True
        with open('server.prop.state','w') as f:
            f.write('1')
        print('Server started at http://localhost:6969')
    sock.close() 

# Define custom filter function to decode URL-encoded string
def url_decode(value):
    return urllib.parse.unquote(value)

@app.route('/')
@app.route('/<path:folder>')
def get_folder_structure(folder=''):
    files = []
    folders = []
    folder = PathManipulator.modify_path(f'{FOLDER_MAIN}/{folder}')
    tree = PathManipulator.generate_directory_tree(folder)['contents']
    for object in tree:
        if object['type'] == 'file':
            files.append(urllib.parse.quote(object['name']))
        if object['type'] == 'directory':
            folders.append(urllib.parse.quote(object['name']))

        

    return render_template('dir.html',files=files,folders=folders)
    

# @app.route('/')
# def main():
#     return render_template('index.html') 

if __name__ == '__main__':
    app.jinja_env.filters['url_decode'] = url_decode
    app.run(port=5000,host='0.0.0.0',debug=True) 