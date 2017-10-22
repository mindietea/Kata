import sys

sys.path.append("../database/Python")

from flask import Flask, jsonify, request, redirect, render_template
import requests
import json
import database
import flask
import vision_recognition
app = Flask(__name__)
import semantics


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


@app.route("/api/post/recommendations/ghome")
def get_recommendations_ghome():
    product_name = request.args.get("name")
    return json.dumps(semantics.get_recommendations(product_name, None))

@app.route("/api/post/recommendations")
def get_recommendations():
    product_name = request.args.get("name")
    try:
        product_brand = request.args.get("brand")
    except:
        return json.dumps(semantics.get_recommendations(product_name))

    return json.dumps(semantics.get_recommendations(product_name, product_brand))

@app.route("/api/post/vision", methods=['POST'])
def get_vision_results():
    image_url = str(request.form['url'])
    return json.dumps(json.loads(vision_recognition.custom_vision_endpoint(image_url)))

@app.route("/api/curator/<curator_id>/posts")
def get_curator_posts(curator_id):
    response = flask.jsonify(database.format_curator(curator_id))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

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
    print(json.loads(following))
    following = json.loads(following)
    for curator in following:
        post_ids = database.get_curator_post_ids(curator["User"])
        for post_id in post_ids:
            feed.append(json.loads(get_post(post_id)))
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

@app.route("/api/post/search", methods=['POST'])
def getItem():
	substring = str(request.form['substring'])
	return database.search_products(substring)

@app.route("/api/post/create_json", methods=['POST'])
def create_custom_json():
    raw_data = json.loads(request.data)
    print request.data
    database.create_post_array(raw_data['curator'], raw_data['title'], raw_data['description'], raw_data['products'])
    return(json.dumps({"status": 200}))

@app.route("/api/post/add_follower", methods=['POST'])
def create_followers():
    body = request.get_json(force=True)
    database.add_follower(body["User"], body["Follower"])
    return(json.dumps({"status": 200}))
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
