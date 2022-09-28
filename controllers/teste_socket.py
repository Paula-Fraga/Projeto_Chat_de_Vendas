from flask_restful import Headers, Resource
from flask import render_template

class TesteSocket(Resource):

    def get(self):
        return render_template('index.html')

    