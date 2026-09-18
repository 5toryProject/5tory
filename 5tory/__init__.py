from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "flaks team project"
    @app.route('/cbi')
    def cbi():
        return render_template('cbi.html')
    return app
