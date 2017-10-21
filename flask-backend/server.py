from flask import Flask, jsonify, request, redirect, render_template
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/post/<post_id>")
def get_post(post_id):
    payload = {
       "post_id": post_id
    }
    response = requests.get(url, params=payload)
    return jsonify(response.json())

@app.route("/api/curator/<curator_id>/posts")
def get_curator_posts(curator_id):
    payload = {
        "curator_id": curator_id
    }
    response = requests.get(url, params=payload)
    return jsonify(response.json())

@app.route("/api/post/create", methods=['POST'])
def create_post():
    body = request.get_json()
    images = body["images"]
    title = body["title"]
    desc = body["description"]
    
    # insert sql connector here

    return jsonify(response.json())
