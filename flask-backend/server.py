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
    for post_id in post_ids:
        curator_posts.append(get_post(post_id))
    return json.dumps({"posts": curator_posts})

@app.route("/api/curator/<curator_id>/following")
def get_followed_curators(curator_id):
    following_ids = database.get_influencers(curator_id)
    return json.dumps({"ids": following_ids})

@app.route("/api/curator/<curator_id>/followers")
def get_following_curators(curator_id):
    follower_ids = database.get_followers(curator_id)
    return json.dumps({"ids": follower_ids})

@app.route("/api/curator/<curator_id>/feed")
def get_feed(curator_id):
    following = database.get_influencers(curator_id)
    feed = []
    for curator in following:
        post_ids = database.get_curator_post_ids(curator)
        for post_id in post_ids:
            feed.append(get_post(post_id))
    return json.dumps({"feed": feed})

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

@app.route("/api/post/create_json", methods=['POST'])
def create_custom_json():
    raw_data = request.get_json()
    print(raw_data)
    database.create_post_array(raw_data['curator'], None, raw_data['title'], raw_data['description'], raw_data['products'])

'''
{
    curator: 0,
    title: "a winter forest"
    description: "a simple yet elegant sweater. will go well with my new boots."
    products: [
        {
            image: "http://img.ltwebstatic.com/images/pi/201708/ee/15028473936476786642.jpg",
            link: "http://us.shein.com/Two-Tone-Ribbed-Pullover-Sweater-p-381441-cat-1734.html",
            title: "Two Tone Ribbed Pullover Sweater, $26.00"
            status: true
        }
    ]
'''
