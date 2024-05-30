import urllib.parse
from flask import *
from pathops import PathManipulator
from net import NetUtils
import urllib
from flask import jsonify
app = Flask(__name__)

# Get local IP address
ipv4_address = NetUtils.get_local_ip()
FOLDER_MAIN = 'C:/Users/Akshit/ELectricCurrent'

SERVER_STARTED = False # legacy method to check if server has been started

SERVER_PORT = 6969

if not SERVER_STARTED:
    NetUtils.server(ipv4_address, SERVER_PORT, FOLDER_MAIN)

     

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

        

    return render_template('dir.html',files=files,folders=folders,server=f'http://{ipv4_address}:{SERVER_PORT}',home= True if folder == [] else False)

# @app.route('/playUrl', methods=['POST'])
# def redirect_to_play():
#     data = request.get_json()
#     url = data['url']
#     print(f'Debugging: {url}') 
#     return "hello"

@app.route('/play')
def play():
    return render_template('player.html', video = request.args.get('video'))

# @app.route('/')
# def main():
#     return render_template('index.html') 

if __name__ == '__main__':
    app.jinja_env.filters['url_decode'] = url_decode
    app.run(port=5000, host='0.0.0.0', debug=True) 
