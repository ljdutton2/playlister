from flask import Flask , render_template,jsonify
app = Flask(__name__)



@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)



if __name__ == '__main__':
    app.debug = True
