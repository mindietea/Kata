from flask import Flask, jsonify, request, redirect, render_template
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/post/<post_id>")
def get_post(post_id):
    return database.get_post(post_id)

@app.route("/api/post/recommendations")
def get_recommendations():
    product_name = requests.args.name,
    product_vendor = requests.args.vendor
    return semantics.get_recommendations(product_name, product_vendor)

@app.route("/api/curator/<curator_id>/posts")
def get_curator_posts(curator_id):
    return database.get_curator_posts(curator_id)

@app.route("/api/post/create", methods=['POST'])
def create_post():
    body = request.get_json()

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
