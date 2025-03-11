from flask import Flask, render_template, request, Response, jsonify

def create_app():
    app = Flask(__name__)
    return app
