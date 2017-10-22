from flask import jsonify, request
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import keys
import json
import requests
import semantics


def custom_vision_endpoint(user_image_url):

    payload = {
      #  "Url": user_image_url
        "Url": "http://www.shadestation.co.uk/media/thumbs/800x800/media/product_images/Rayban-Glasses-RX5227-2034afw800fh800.png"
    }
    headers = {
        "Content-Type": "application/json",
        "Prediction-Key": "66aaad81eed9481bba65df01dfe09420"
    }

    url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v1.0/Prediction/91f2d2f7-5c8d-4eb3-a741-a9c75ab6fc41/url"
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response = response.json()
    # if custom model has high probability rate, return recommendations
    if response['Predictions'][0]['Probability'] > 1.75:
        val = response['Predictions'][0]['Tag']
        print(val)
        return semantics.get_recommendations(val)
    # call clarifai api otherwise
    else:
        k = keys.Keys()
        app = ClarifaiApp(api_key=k.get_clarifai_key())
        # Use apparel model
        model = app.models.get('apparel')
        image = ClImage(url = user_image_url)
        result= model.predict([image])
        concepts = result['outputs'][0]['data']['concepts']
        # check for high confidence
        if concepts[0]['value'] >= .9:
            val = concepts[0]['name']
            return semantics.get_recommendations(val)

custom_vision_endpoint("http://www.shadestation.co.uk/media/thumbs/800x800/media/product_images/Rayban-Glasses-RX5227-2034afw800fh800.png")