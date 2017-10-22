import sys

sys.path.append("../database/Python")

from flask import Flask, jsonify, request, redirect, render_template
import requests
import json
import database
import semantics
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/post/<post_id>")
def get_post(post_id):
    post_info = database.get_post(post_id)
    product_info = database.get_product(post_id)
    image_info = database.get_image(post_id)
    result = json.loads(post_info)
    result[0]["products"] = product_info
    result[0]["images"] = image_info
    print(str(result[0]))
    return json.dumps(result[0])


@app.route("/api/post/recommendations")
def get_recommendations():
    product_name = request.args.get("name")
    product_brand = request.args.get("brand")
    return json.dumps(semantics.get_recommendations(product_name, product_brand))

@app.route("/api/curator/<curator_id>/posts")
def get_curator_posts(curator_id):
    post_ids = database.get_curator_post_ids(curator_id)
    curator_posts = []
    for id in post_ids:
        curator_posts.append(get_post(id))
    return json.dumps({"posts": curator_posts})

@app.route("/api/post/create", methods=['POST'])
def create_post():
    body = request.get_json(force=True)

    curator = body["curator"]
    date = body["date"]
    title = body["title"]
    desc = body["description"]
    in_stock = body["in_stock"]
    sizes = body["sizes"]
    product_link = body["product_link"]
    product_name = body["product_name"]
    image_link = body["image"]
    image_name = body["image_name"]

    database.create_post(curator, date, title, desc, in_stock, sizes, product_link, product_name, image_link, image_name)

    return(json.dumps({"status": 200}))
