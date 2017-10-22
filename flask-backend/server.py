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
    return "test"


@app.route("/api/post/recommendations")
def get_recommendations():
    product_name = request.args.get("name")
    product_brand = request.args.get("brand")
    return json.dumps(semantics.get_recommendations(product_name, product_brand))

@app.route("/api/curator/<curator_id>/posts")
def get_curator_posts(curator_id):
    return database.get_curator_posts(curator_id)

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
    return database.create_post(curator, date, title, desc, in_stock, sizes, product_link, product_name, image_link, image_name)

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
