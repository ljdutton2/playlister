from flask import Flask , render_template,jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template

@app.route('/playlists')
def playlists_index():
    """Show all playlists."""



if __name__ == '__main__':
    app.debug = True
