from flask import jsonify
from flask import Flask
from flask_restful import Resource, Api

import models


class ScrapedData(Resource):
    def get(self):
        # scraped reddit post
        return jsonify({'scraped_data': []})