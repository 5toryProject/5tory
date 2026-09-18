from alembic.autogenerate import render
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "flaks team project"

    @app.route('/ysb')
    def ysb():
        return render_template('ysb.html')
    return app