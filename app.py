import bottle
import requests
from bottle import request, post, get, hook, response, static_file
import os
from lib.utils import load_json


app = bottle.app()
app_conf = load_json("./conf.json")["app"]


@app.route("/api/dm/order/new", method=["POST"])
def new_order():
    pass


@app.route("/api/dm/order/status/<order_id>", method=["GET"])
def order_status(order_id):
    pass


@app.route("/api/algo/extract", method=["POST"])
def extract():
    pass


@app.route("/api/algo/query_kg", method=["GET"])
def query_kg():
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=11451, debug=True)
