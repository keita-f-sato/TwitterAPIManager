import threading
import tweepy
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from .bot import Controller, TwitterIdStore


app = Flask(__name__)
api = Api(app)

twitter_bots = dict()


def add_id_list(value):
    if value in twitter_bots.keys():
        return False
    twitter_bots.add(value)
    return True


class TwitterQue(Resource):
    def post(self):
        twitter_info = request.json

        if add_id_list(twitter_info["id"]):
            twitter_bots[twitter_info["id"]] = TwitterIdStore(twitter_info)
            return {"status": "true"}, 200
        return {"status": "false"}, 400

    def get(self):
        return {'hello': 'world'}

    def delete(self):
        twitter_info = request.json
        twitter_bots[twitter_info["id"]].stop()

        return {'hello': 'world'}


class QueList(Resource):
    def get(self):
        return {"Lists": [i.twitter_id for i in twitter_bots.keys()]}

api.add_resource(TwitterQue, '/')
api.add_resource(QueList, '/list')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
