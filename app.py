from flask import Flask , render_template
app = Flask(__name__)

@approute('/')
def index():
    return render_template

if __name__ == '__main__':
    
